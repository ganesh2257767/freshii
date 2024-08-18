from flask import Flask, render_template, request, url_for, flash
import mysql.connector
from mysql.connector.errors import IntegrityError

mydb = mysql.connector.connect(
    host="mysql.railway.internal",
    user="root",
    password="AlciOgdqfDZHzmBWPtuGDrYpuglPEqme",
    database="railway"
)

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="freshii"
# )

app = Flask(__name__, template_folder="templates",
            static_folder="static", static_url_path="/")

app.config[
    'SECRET_KEY'] = 'hhLlPl"0aku}Yh0dk^FDJ-=Vq&V>;S=0h1~5j2Zct4M>X$:ZoWSJ-__(B3jLuV('


cursor = mydb.cursor(buffered=True)
def refresh_data():
    cursor.execute("SELECT * from freshii_daily")
    data = cursor.fetchall()
    return data

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form_data = request.form

        sql = "INSERT INTO freshii_daily (date, c1, c5, c10, c25, c50, d1, d2, d5, d10, d20, d50, d100, bag_amount, locker_amount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (form_data["date"], form_data["c1"], form_data["c5"], form_data["c10"], form_data["c25"], form_data["c50"], form_data["d1"], form_data["d2"],
               form_data["d5"], form_data["d10"], form_data["d20"], form_data["d50"], form_data["d100"], form_data["bag"], form_data["locker"])

        try:
            cursor.execute(sql, val)
        except IntegrityError as e:
            flash(f'Data for this date: {form_data["date"]} already exists', 'error')

        mydb.commit()

    data = refresh_data()
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
