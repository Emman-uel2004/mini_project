from flask import Blueprint, render_template, request, redirect, session
import mysql.connector

admin_bp = Blueprint("admin", __name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",
    database="login_db"
)
# ADMIN LOGIN
@admin_bp.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    error = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM admin WHERE username = %s AND password = %s",
            (username, password)
        )
        admin = cursor.fetchone()
        cursor.close()
        if admin:
            session["admin_id"] = admin["id"]
            session["admin_username"] = admin["username"]
            return redirect("/admin/dashboard")
        else:
            error = "Invalid username or password"
    return render_template(
        "admin_login.html",
        error=error
    )
# ADMIN DASHBOARD
@admin_bp.route("/admin/dashboard")
def admin_dashboard():

    if "admin_id" not in session:
        return redirect("/admin/login")
    cursor = db.cursor(dictionary=True)
    # TOTAL STUDENTS
    cursor.execute(
        "SELECT COUNT(*) AS total FROM `user`"
    )
    total_students = cursor.fetchone()["total"]
    # SSLC AVERAGE
    cursor.execute(
        "SELECT AVG(percentage) AS average FROM sslc"
    )
    sslc_average = cursor.fetchone()["average"] or 0
    # HSC AVERAGE
    cursor.execute(
        "SELECT AVG(percentage) AS average FROM hsc"
    )
    hsc_average = cursor.fetchone()["average"] or 0
    # UG AVERAGE
    cursor.execute(
        "SELECT AVG(ug_percentage) AS average FROM ug"
    )
    ug_average = cursor.fetchone()["average"] or 0
    # GENDER DATA
    cursor.execute("""
        SELECT gender, COUNT(*) AS count
        FROM persnol
        WHERE gender IS NOT NULL
        AND gender != ''
        GROUP BY gender
    """)
    gender_data = cursor.fetchall()
    # ADMISSION TYPE DATA
    cursor.execute("""
        SELECT admission_type, COUNT(*) AS count
        FROM persnol
        WHERE admission_type IS NOT NULL
        AND admission_type != ''
        GROUP BY admission_type
    """)

    admission_data = cursor.fetchall()
    # PASSING YEAR DATA
    cursor.execute("""
        SELECT passing_year, COUNT(*) AS count
        FROM sslc
        WHERE passing_year IS NOT NULL
        GROUP BY passing_year
        ORDER BY passing_year
    """)
    passing_year_data = cursor.fetchall()
    cursor.close()
    # SEND DATA TO HTML
    return render_template(
        "admin.html",
        total_students=total_students,
        sslc_average=round(float(sslc_average), 2),
        hsc_average=round(float(hsc_average), 2),
        ug_average=round(float(ug_average), 2),
        gender_data=gender_data,
        admission_data=admission_data,
        passing_year_data=passing_year_data
    )
# ADMIN LOGOUT
@admin_bp.route("/admin/logout")
def admin_logout():
    session.pop("admin_id", None)
    session.pop("admin_username", None)
    return redirect("/admin/login")