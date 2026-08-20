from flask import Blueprint, render_template, request, redirect, session
import mysql.connector
import re

login_bp = Blueprint("login", __name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",
    database="login_db"
)


@login_bp.route("/")
def home():
    return render_template("login.html")


@login_bp.route("/register")
def register():
    return render_template("register.html")


@login_bp.route("/register", methods=["POST"])
def register_user():

    fullname = request.form["fullname"]
    username = request.form["username"]
    password = request.form["password"]

    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one capital letter"

    if not re.search(r"[a-z]", password):
        return "Password must contain at least one small letter"

    if not re.search(r"[0-9]", password):
        return "Password must contain at least one number"

    if not re.search(r"[@$!%*?&]", password):
        return "Password must contain at least one special character"

    if len(password) < 8:
        return "Password must be at least 8 characters"

    email = request.form["email"]

    cursor = db.cursor()

    sql = """
    INSERT INTO user (fullname, username, password, email)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (fullname, username, password, email))

    db.commit()
    cursor.close()

    return redirect("/")


@login_bp.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    # dictionary=True is important
    cursor = db.cursor(dictionary=True, buffered=True)

    query = "SELECT * FROM user WHERE username=%s AND password=%s"

    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    cursor.close()

    if user:

        session["user_id"] = user["id"]

        current_step = user["current_step"]

        if current_step == "personal":
            return redirect("/persnol")

        elif current_step == "sslc":
            return redirect("/sslc")

        elif current_step == "hsc":
            return redirect("/hsc")

        elif current_step == "ug":
            return redirect("/ug")

        elif current_step == "pg":
            return redirect("/pg")

        elif current_step == "completed":
            return redirect("/dashboard")
        

        else:
            return redirect("/persnol")

    else:
        return "<h2>Invalid Username or Password</h2>"


