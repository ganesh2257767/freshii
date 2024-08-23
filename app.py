from flask import Flask, render_template, request, url_for, flash, redirect
import mysql.connector
from mysql.connector.errors import IntegrityError
import os
import dotenv

dotenv.load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DB")
)

app = Flask(__name__, template_folder="templates",
            static_folder="static", static_url_path="/")

app.config[
    'SECRET_KEY'] = 'hhLlPl"0aku}Yh0dk^FDJ-=Vq&V>;S=0h1~5j2Zct4M>X$:ZoWSJ-__(B3jLuV('


cursor = mydb.cursor(buffered=True)
def refresh_data():
    cursor.execute("SELECT * from freshii_daily")
    data = cursor.fetchall()
    return data

def insert_data(form_data):
    sql = "INSERT INTO freshii_daily (date, c1, c5, c10, c25, c50, d1, d2, d5, d10, d20, d50, d100, bag_amount, locker_amount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = [form_data.get(key) if value else '0' for key, value in form_data.items()]
    print(val)
    try:
        cursor.execute(sql, val)
    except IntegrityError as e:
        return False
    except Exception as e:
        return f"{type(e) - str(e)}"
    else:
        mydb.commit()
        return True
    
def update_data(form_data):
    sql = "UPDATE freshii_daily SET c1 = %s, c5 = %s, c10 = %s, c25 = %s, c50 = %s, d1 = %s, d2 = %s, d5 = %s, d10 = %s, d20 = %s, d50 = %s, d100 = %s, bag_amount = %s, locker_amount = %s WHERE date = %s"
    val_temp = [form_data.get(key) if value else '0' for key, value in form_data.items()]
    val = val_temp[1:] + [val_temp[0]]
    try:
        cursor.execute(sql, val)
    except Exception as e:
        return False
    else:
        mydb.commit()
        return True


def delete_data(date):
    sql = "DELETE FROM freshii_daily WHERE date = %s"
    val = [date]
    try:
        cursor.execute(sql, val)
    except Exception as e:
        return False
    else:
        mydb.commit()
        return True

@app.route("/dashboard", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        data = refresh_data()
        return render_template("index.html", data=data)
    
    if request.method == "POST":
        form_data = request.form
        if not insert_data(form_data):
            if update_data(form_data):
                flash(f'Data for this date: {form_data["date"]} already exists, data has been updated', 'info')
            else:
                flash("Something went wrong, please try again", 'danger')
        else:
            flash('Data added successfully', 'success')
        return redirect(url_for("index"))
    
@app.route("/", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/delete/<date>", methods=["GET", "POST"])
def delete(date):
    if delete_data(date):
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
