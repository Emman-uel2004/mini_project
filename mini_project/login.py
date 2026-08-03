from flask import Blueprint, render_template, request, redirect
import mysql.connector

login_bp=Blueprint("login",__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",   # unga MySQL password
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

    cursor = db.cursor(buffered=True)

    query = "SELECT * FROM user WHERE username=%s AND password=%s"

    cursor.execute(query, (username, password))

    user = cursor.fetchone() 

    

    if user:
        return redirect("/persnol")
    else:
        return "<h2>Invalid Username or Password</h2>"


