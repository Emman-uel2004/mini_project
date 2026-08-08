from flask import Blueprint, render_template, request, redirect
import mysql.connector


hsc_bp = Blueprint("hsc", __name__)


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",
    database="login_db"
)


@hsc_bp.route("/hsc", methods=["GET", "POST"])
def twelfth_mark():

    if request.method == "POST":

        board = request.form.get("board")
        group = request.form.get("group")

        tamil = request.form.get("tamil") or None
        english = request.form.get("english") or None
        mathematics = request.form.get("mathematics") or None
        physics = request.form.get("physics") or None
        chemistry = request.form.get("chemistry") or None
        computer_science = request.form.get("computer_science") or None

        biology = request.form.get("biology") or None

        accountancy = request.form.get("accountancy") or None
        commerce = request.form.get("commerce") or None
        economics = request.form.get("economics") or None
        computer_applications = request.form.get("computer_applications") or None

        history = request.form.get("history") or None
        political_science = request.form.get("political_science") or None
        geography = request.form.get("geography") or None

        total = request.form.get("total") or 0
        percentage = request.form.get("percentage") or "0"

        percentage = percentage.replace("%", "")
        exam_written= request.form["exam_written"]
        subject_written=request.form["subject_written"]
        medium_of_instruction =request.form["medium_of_instruction"]
        school_name =request.form["school_name"]
        passing_year= request.form["passing_year"]
        certificate_sl_no= request.form["certificate_sl_no"]



        cursor = db.cursor()


        sql = """
        INSERT INTO hsc
        (
            board,
            group_name,
            tamil,
            english,
            mathematics,
            physics,
            chemistry,
            computer_science,
            biology,
            accountancy,
            commerce,
            economics,
            computer_applications,
            history,
            political_science,
            geography,
            total,
            percentage,
            exam_written,
            subject_written,
            medium_of_instruction,
            school_name,
            passing_year,
            certificate_sl_no
        )
        VALUES
        (
            %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s,%s,%s,%s,%s,%s
        )
        """


        values = (
            board,
            group,
            tamil,
            english,
            mathematics,
            physics,
            chemistry,
            computer_science,
            biology,
            accountancy,
            commerce,
            economics,
            computer_applications,
            history,
            political_science,
            geography,
            total,
            percentage,
            exam_written,
            subject_written,
             medium_of_instruction,
            school_name,
            passing_year,
            certificate_sl_no
        )


        cursor.execute(sql, values)

        db.commit()

        cursor.close()


        return redirect("/dashboard")


    return render_template("hsc.html")


@hsc_bp.route("/dashboard")
def dashboard():

    return "Registration Successful!"