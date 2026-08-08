from flask import Blueprint, render_template, request,redirect, session
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

@persnol_bp.route("/persnol", methods=["POST"])
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

      # Login pannina user ID
    user_id = session["user_id"]

    # Next step = SSLC
    cursor.execute(
        "UPDATE user SET current_step = %s WHERE id = %s",
        ("sslc", user_id)
    )

    db.commit()
    cursor.close()

    return redirect("/sslc")







    