from flask import Blueprint, render_template, request, redirect
import mysql.connector
sslc_bp=Blueprint("sslc",__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",   # unga MySQL password
    database="login_db"
)
@sslc_bp.route("/sslc")
def home():
    return render_template("sslc.html")

@sslc_bp.route("/sslc", methods=["POST"])
def register_user():
       name= request.form["name"]
    initial   = request.form["initial"]
    father_name = request.form["father_name"]
    mother_name = request.form["mother_name"]
    blood_group = request.form["blood_group"]
    admission_type = request.form["admission_type"]
    contact = request.form["contact"]
    mother_tongue = request.form["mother_tongue"]
    gender = request.form["gender"]
    email = request.form["email"]
    nationality = request.form["nationality"]
    aadhar = request.form["aadhar"]
    cast = request.form["cast"]
    dob = request.form["dob"]


    cursor = db.cursor()

    sql = """
    INSERT INTO persnol (name, initial, father_name, mother_name, blood_group, admission_type, contact, mother_tongue, dob, cast, aadhar, nationality, email, gender)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,%s, %s, %s)
    """

    cursor.execute(sql, (name, initial, father_name, mother_name, blood_group, admission_type, contact, mother_tongue, dob, cast, aadhar, nationality, email, gender))

    db.commit()
    cursor.close()