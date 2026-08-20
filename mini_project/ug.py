from flask import Blueprint, render_template, request, redirect,session
import mysql.connector
ug_bp=Blueprint("ug",__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",   # unga MySQL password
    database="login_db"
)
@ug_bp.route("/ug")
def home():
    return render_template("ug.html")

@ug_bp.route("/ug", methods=["POST"])
def register_user():
    user_id=session["user_id"]


    ug_degree =request.form["ug_degree"]
    ug_percentage =request.form["ug_percentage"]
    consolidated_certificate =request.form["consolidated_certificate"]
    provisional_certificate =request.form["provisional_certificate"]
    ug_class=request.form["ug_class"]
    ug_college=request.form["ug_college"]
    university=request.form["university"]
    year_of_passing=request.form["year_of_passing"]


    cursor = db.cursor()

    cursor.execute("select id from ug where user_id=%s" ,(user_id,)  )
    existing=cursor.fetchone()

    if existing:
        sql=""" update ug set ug_degree=%s,ug_percentage=%s ,consolidated_certificate=%s,provisional_certificate=%s,ug_class=%s,ug_college=%s,university=%s,year_of_passing=%s where user_id=%s"""
        cursor.execute(sql,(ug_degree,ug_percentage ,consolidated_certificate,provisional_certificate,ug_class,ug_college,university,year_of_passing,user_id))

    else:
        sql = """
    INSERT INTO ug (ug_degree,ug_percentage ,consolidated_certificate,provisional_certificate,ug_class,ug_college,university,year_of_passing,user_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s ,%s  )
    """
        cursor.execute(sql, (ug_degree,ug_percentage ,consolidated_certificate,provisional_certificate,ug_class,ug_college,university,year_of_passing, user_id))
        

    db.commit()

    cursor.close()
    return redirect("/dashboard")





@ug_bp.route("/dashboard")
def dashboard():

    return "Registration Successful!"
