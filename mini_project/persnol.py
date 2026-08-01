from flask import Flask, render_template, request,redirect
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",   # unga MySQL password
    database="login_db"
)

@app.route("/")
def home():
    return render_template("persnol.html")

@app.route("/register", methods=["POST"])
def register_user():

    Fullname= request.form["Fullname"]
    DOB = request.form["DOB"]
    Gender = request.form["Gender"]
    Email = request.form["Email"]
    Mobile = request.form["Mobile"]
    Address = request.form["Address"]


    cursor = db.cursor()

    sql = """
    INSERT INTO persnol (Fullname, DOB, Gender, Email, Mobile, Address)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (Fullname, DOB, Gender, Email,Mobile, Address))

    db.commit()
    cursor.close()

    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    return "<h1>Registration Successful!</h1>"



if __name__ == "__main__":
    app.run(debug=True)

    