from flask import Blueprint, render_template, request,redirect
import mysql.connector

persnol_bp = Blueprint("persnol",__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",   # unga MySQL password
    database="login_db"
)

@persnol_bp.route("/persnol")
def home():
    return render_template("persnol.html")

@persnol_bp.route("/register", methods=["POST"])
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

@persnol_bp.route("/dashboard")
def dashboard():
    return "<h1>Registration Successful!</h1>"





    