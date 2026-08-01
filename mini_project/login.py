from flask import Flask, render_template, request, redirect
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
    return render_template("login.html")
    
@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
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

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    cursor = db.cursor(buffered=True)

    query = "SELECT * FROM user WHERE username=%s AND password=%s"

    cursor.execute(query, (username, password))

    user = cursor.fetchone() 

    

    if user:
        return redirect("/dashboard")
    else:
        return "<h2>Invalid Username or Password</h2>"


@app.route("/dashboard")
def dashboard():
    return "<h1>Welcome! Login Successful</h1>"


if __name__ == "__main__":
    app.run(debug=True)