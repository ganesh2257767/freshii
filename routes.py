from flask import render_template, request, url_for, redirect, flash, session
from models import User, FreshiiData
from sqlalchemy.exc import IntegrityError

def register_routes(app, db, bcrypt):
    @app.route("/dashboard", methods=["GET", "POST"])
    def dashboard():
        if request.method == "GET":
            data = FreshiiData.query.all()
            return render_template("dashboard.html", data=data)
        
        if request.method == "POST":
            form_data = {k: v if v else 0 for k, v in dict(request.form).items()}
            print(form_data)

            data = FreshiiData(**form_data)
            db.session.add(data)
            try:
                db.session.commit()
            except IntegrityError as e:
                db.session.rollback()
                update_form_data = dict(list(form_data.items())[1:])
                data = FreshiiData.query.filter_by(date=form_data["date"]).update(update_form_data)
                try:
                    db.session.commit()
                except Exception as e:
                    flash(f'Unknown Exception {type(e)} - {str(e)}', 'error')
                else:
                    flash(f'Data for this date: {form_data["date"]} already exists, data has been updated.', 'info')
            else:
                flash('Data added successfully.', 'success')
            return redirect(url_for("dashboard"))
    
    @app.route("/", methods=["GET", "POST"])
    def login():
        return render_template("login.html")


    @app.route("/delete/<date>", methods=["GET"])
    def delete(date):
        FreshiiData.query.filter(FreshiiData.date == date).delete()
        try:
            db.session.commit()
        except Exception as e:
            flash(f'Unknown Exception {type(e)} - {str(e)}', 'error')
        else:
            flash('Data deleted successfully.', 'success')
            return redirect(url_for("dashboard"))
