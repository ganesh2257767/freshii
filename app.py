from flask import Flask, render_template, request, url_for, flash
from flask_mysqldb import MySQL
from MySQLdb import IntegrityError

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/")

app.config['SECRET_KEY'] = 'hhLlPl"0aku}Yh0dk^FDJ-=Vq&V>;S=0h1~5j2Zct4M>X$:ZoWSJ-__(B3jLuV('

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'freshii'
# mysql.init_app(app)
mysql = MySQL(app)


@app.route("/", methods=["GET", "POST"])
def index():

    with mysql.connection.cursor() as cursor:
        cursor.execute("SELECT * from freshii_daily")
        data = cursor.fetchone()
        
    if request.method == "GET":
        return render_template("index.html")
    
    if request.method == "POST":
        data = request.form
        
        sql = "INSERT INTO freshii_daily (date, c1, c5, c10, c25, c50, d1, d2, d5, d10, d20, d50, d100, bag_amount, locker_amount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (data["date"], data["c1"], data["c5"], data["c10"], data["c25"], data["c50"], data["d1"], data["d2"], data["d5"], data["d10"], data["d20"], data["d50"], data["d100"], data["bag"], data["locker"])
        
        with mysql.connection.cursor() as cursor:
            try:
                cursor.execute(sql, val)
            except IntegrityError as e:
                flash(f'Data for this date: {data["date"]} already exists', 'error')
                
        mysql.connection.commit()
    
    print(data)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)