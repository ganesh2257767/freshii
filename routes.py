from flask import render_template, request, url_for, redirect, flash
from models import User, FreshiiData
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.exceptions import HTTPException

def register_routes(app, db, bcrypt):
    @app.route("/dashboard", methods=["GET", "POST"])
    @login_required
    def dashboard():
        if request.method == "GET":
            data = FreshiiData.query.all()
            return render_template("dashboard.html", data=data)
        
        if request.method == "POST":
            form_data = {k: v if v else 0 for k, v in dict(request.form).items()}
            print(form_data)
            
            data = FreshiiData(**form_data, **{"entered_by_user_id": current_user.id})
            db.session.add(data)
            try:
                db.session.commit()
            except IntegrityError as e:
                db.session.rollback()
                update_form_data = dict(list(form_data.items())[1:]) | {"updated_by_user_id": current_user.id}
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
    @app.route("/login", methods=["GET", "POST"])
    def login():
        print("Login called", request.method)
        if request.method == "GET":
            print("Login called", request.method)
            return render_template("login.html")
        
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            print(username, password)

            user = User.query.filter_by(username=username).first()
            print(user)
            if not user:    
                flash("Invalid credentials. Please try again.", "danger")
                return redirect(url_for("login"))
                   
            if bcrypt.check_password_hash(user.password, password):
                print("Paswword hash compared")
                login_user(user)
                print("User logged in successfully")
                return redirect(url_for("dashboard"))
            
            flash("Invalid credentials. Please try again.", "danger")
            return redirect(url_for("login"))
                

    @app.route("/logout", methods=["GET"])
    def logout():
        logout_user()
        flash("Logged out successfully.", "success")
        return redirect(url_for("login"))

    
    @app.errorhandler(Exception)
    def page_not_found(e):
        if isinstance(e, HTTPException):
            if e.code == 401:
                flash("Unauthorized, please login first.", "danger")
                return redirect(url_for("login"))
            if e.code == 404:
                return """<h1>Not Found</h1>""", 404
    
    # These routes are not required, will be using the Admin panel to add, update and delete users
    # @app.route("/delete/<date>", methods=["GET"])
    # def delete(date):
    #     FreshiiData.query.filter(FreshiiData.date == date).delete()
    #     try:
    #         db.session.commit()
    #     except Exception as e:
    #         flash(f'Unknown Exception {type(e)} - {str(e)}', 'error')
    #     else:
    #         flash('Data deleted successfully.', 'success')
    #     return redirect(url_for("login"))
    
    
    # @app.route("/register", methods=["GET", "POST"])
    # def register():
    #     if request.method == "GET":
    #         return render_template("register.html")
    #     if request.method == "POST":
    #         username = request.form.get("username")
    #         hashed_password = bcrypt.generate_password_hash(request.form.get("password")).decode("utf-8")
            
    #         user = User(username=username, password=hashed_password, role="admin")
            
    #         db.session.add(user)
    #         db.session.commit()
            
    #         flash("User created successfully.", "success")
    #         return render_template("register.html")