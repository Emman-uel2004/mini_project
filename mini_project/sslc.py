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
    language1_mark= request.form["language1_mark"]
    language2_mark   = request.form["language2_mark"]
    mathematics_mark = request.form["mathematics_mark"]
    science_mark = request.form["science_mark"]
    social_science_mark = request.form["social_science_mark"]
    exam_written = request.form["exam_written"]
    total_mark = request.form["total_mark"]
    medium_of_instruction = request.form["medium_of_instruction"]
    subject_written = request.form["subject_written"]
    school_name = request.form["school_name"]
    passing_year = request.form["passing_year"]
    certificate_sl_no = request.form["certificate_sl_no"]
    percentage = request.form["percentage"]
    


    cursor = db.cursor()

    sql = """
    INSERT INTO sslc (language1_mark,language2_mark,mathematics_mark,science_mark,social_science_mark,exam_written,total_mark,medium_of_instruction,subject_written,school_name,passing_year,certificate_sl_no,percentage)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,%s,%s)
    """

    cursor.execute(sql, (language1_mark,language2_mark,mathematics_mark,science_mark,social_science_mark,exam_written,total_mark,medium_of_instruction,subject_written,school_name,passing_year,certificate_sl_no,percentage))

    db.commit()
    cursor.close()

    return redirect("/dashboard")

@sslc_bp.route("/dashboard")
def dashboard():
    return "<h1>Registration Successful!</h1>"