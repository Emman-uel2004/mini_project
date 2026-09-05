from flask import Blueprint, render_template, request,redirect, session
import mysql.connector
import re

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
    user_id=session["user_id"]

    cursor = db.cursor(dictionary=True)

    if request.method == "GET": cursor.execute("SELECT * FROM persnol WHERE user_id=%s",(session["user_id"],))
    data = cursor.fetchone()
      
    return render_template("persnol.html",form=data or {},errors = {})

@persnol_bp.route("/persnol", methods=["POST"])
def register_user():
    
    errors = {}

    name= request.form["name"]
    if not name.strip():
        errors["name"] = "Name cannot be empty"
    elif not re.fullmatch(r"[A-Za-z ]+", name):
         errors["name"] = "Invalid name"

    initial   = request.form["initial"]
    if not initial.strip():
        errors["initial"] = "initial cannot be empty"
    elif not re.fullmatch(r"[A-Za-z ]+", initial):
        errors["initial"] = "Invalid initial"
    
    father_name = request.form["father_name"]
    if not father_name.strip():
        errors["father_name"] = "father_name cannot be empty"
    elif not re.fullmatch(r"[A-Za-z ]+", father_name):
        errors["father_name"] = "Invalid father_name"
   
    mother_name = request.form["mother_name"]
    if not mother_name.strip():
        errors["mother_name"] = "mother_name cannot be empty"
    elif not re.fullmatch(r"[A-Za-z ]+", mother_name):
        errors["mother_name"] = "Invalid mother_name"
    
    blood_group = request.form["blood_group"]
    if blood_group not in ["A+", "A-", "B+", "B-", "O+", "O-"]:
        errors["blood_group"] = "Please select blood group"
    
    admission_type = request.form["admission_type"]
    if admission_type not in ["Management", "Government"]:
        errors["admission_type"] = "Please select admission type"
    
    contact = request.form["contact"]
    if not contact.strip():
        errors["contact"] = "contact cannot be empty"
    elif not re.fullmatch(r"[6-9][0-9]{9}", contact):
        errors["contact"] = "Invalid contact number"
   
    email = request.form["email"]
    if not email.strip():
        errors["email"] = "Email cannot be empty"
    elif not re.fullmatch(r"[a-z0-9._%+-]+@gmail\.com", email):
        errors["email"] = "Invalid email"

    mother_tongue = request.form["mother_tongue"]
    if not mother_tongue.strip():
        errors["mother_tongue"] = "mother_tongue cannot be empty"
    elif not re.fullmatch(r"[A-Za-z ]+", mother_tongue):
        errors["mother_tongue"] = "Invalid mother_tongue"
    
    gender = request.form["gender"]
    if gender not in ["male", "femal", "others"]:
        errors["gender"] = "Please select gender"
    
    nationality = request.form["nationality"]
    if nationality not in ["india", "usa", "canada","africa","barginofao","nigeriya"]:
        errors["nationality"] = "Please select nationality"
    aadhar = request.form["aadhar"]
    if not aadhar.strip():
        errors["aadhar"] = "aadhar cannot be empty"
    elif not re.fullmatch(r"[0-9]{12}", aadhar):
        errors["aadhar"] = "Aadhar number must contain exactly 12 digits"
    cast = request.form["cast"]
    if not cast.strip():
        errors["cast"] = "cast cannot be empty"
    elif not re.fullmatch(r"[A-Za-z ]+", cast):
        errors["cast"] = "Invalid cast"
    dob = request.form["dob"]
    if not dob.strip():
        errors["dob"] = "Date of Birth cannot be empty"

    if errors:
        return render_template("persnol.html", errors=errors, form=request.form)


    cursor = db.cursor()

    cursor.execute( "SELECT id FROM persnol WHERE user_id = %s", (user_id,) )
    
    existing= cursor.fetchone()

    if existing:
        sql="""UPDATE persnol set name=%s, initial=%s, father_name=%s, mother_name=%s, blood_group=%s, admission_type=%s, contact=%s, mother_tongue=%s, dob=%s, cast=%s, aadhar=%s, nationality=%s, email=%s, gender=%s where user_id=%s """

        
        cursor.execute(sql,( name, initial, father_name, mother_name, blood_group, admission_type, contact, mother_tongue, dob, cast, aadhar, nationality, email, gender,user_id))
    else:
        sql = """
        INSERT INTO persnol (name, initial, father_name, mother_name, blood_group, admission_type, contact, mother_tongue, dob, cast, aadhar, nationality, email, gender ,user_id)
        VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s,%s, %s, %s)
        """
        cursor.execute(sql, (name, initial, father_name, mother_name, blood_group, admission_type, contact, mother_tongue, dob, cast, aadhar, nationality, email, gender ,user_id))



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







    