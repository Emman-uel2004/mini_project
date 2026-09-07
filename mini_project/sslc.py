from flask import Blueprint, render_template, request, redirect, session
import mysql.connector
import re
sslc_bp=Blueprint("sslc",__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",   # unga MySQL password
    database="login_db"
)
@sslc_bp.route("/sslc")
def home():
    user_id=session.get("user_id")

    cursor = db.cursor(dictionary=True)

    if request.method == "GET": cursor.execute("SELECT * FROM sslc WHERE user_id=%s",(session["user_id"],))
    data = cursor.fetchone()
      
    
    return render_template("sslc.html",form=data or {},errors = {})

@sslc_bp.route("/sslc", methods=["POST"])
def register_user():
    user_id=session["user_id"]
   
    errors = {}

    language1_mark= request.form["language1_mark"]
    if not language1_mark.strip():
        errors["language1_mark"] = "language1_mark cannot be empty"
    

    language2_mark   = request.form["language2_mark"]
    if not language2_mark.strip():
        errors["language2_mark"] = "language2_mark cannot be empty"
    

    mathematics_mark = request.form["mathematics_mark"]
    if not mathematics_mark.strip():
        errors["mathematics_mark"] = "mathematics_mark cannot be empty"
   

    science_mark = request.form["science_mark"]
    if not science_mark.strip():
        errors["science_mark"] = "science_mark cannot be empty"
    

    social_science_mark = request.form["social_science_mark"]
    if not social_science_mark.strip():
        errors["social_science_mark"] = "social_science_mark cannot be empty"
    

    exam_written = request.form["exam_written"]
    if not exam_written.strip():
        errors["exam_written"] = "exam_written cannot be empty"

    total_mark = request.form["total_mark"]
    
    medium_of_instruction = request.form["medium_of_instruction"]
    if not medium_of_instruction.strip():
        errors["medium_of_instruction"] = "medium_of_instruction cannot be empty"

    subject_written = request.form["subject_written"]
    if not subject_written.strip():
        errors["subject_written"] = "subject_written cannot be empty"
        
    school_name = request.form["school_name"]
    if not school_name.strip():
        errors["school_name"] = "school_name cannot be empty"
        
    passing_year = request.form["passing_year"]
    if not passing_year.strip():
        errors["passing_year"] = "passing_year cannot be empty"
    elif not passing_year.isdigit():
        errors["passing_year"] = "passing year mark must contain numbers only"
        
    certificate_sl_no = request.form["certificate_sl_no"]
    if not certificate_sl_no.strip():
        errors["certificate_sl_no"] = "certificate_sl_no cannot be empty"
        
    percentage = request.form["percentage"]
    

    tenth_board = request.form["tenth_board"]
    if not tenth_board.strip():
        errors["tenth_board"] = "tenth_board cannot be empty"

    if errors:
        return render_template("sslc.html", errors=errors, form=request.form)
    


    cursor = db.cursor()

    cursor.execute( "SELECT id FROM sslc WHERE user_id = %s", (user_id,) )

    existing= cursor.fetchone()

    if existing:
        sql="""update sslc set language1_mark=%s,language2_mark=%s,mathematics_mark=%s,science_mark=%s,social_science_mark=%s,exam_written=%s,total_mark=%s,medium_of_instruction=%s,subject_written=%s,school_name=%s,passing_year=%s,certificate_sl_no=%s,percentage=%s,tenth_board=%s where user_id=%s"""
        cursor.execute(sql, (language1_mark,language2_mark,mathematics_mark,science_mark,social_science_mark,exam_written,total_mark,medium_of_instruction,subject_written,school_name,passing_year,certificate_sl_no,percentage,tenth_board,user_id))
    else:
        sql = """
    INSERT INTO sslc (language1_mark,language2_mark,mathematics_mark,science_mark,social_science_mark,exam_written,total_mark,medium_of_instruction,subject_written,school_name,passing_year,certificate_sl_no,percentage,tenth_board,user_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,%s,%s,%s,%s)
    """
        cursor.execute(sql, (language1_mark,language2_mark,mathematics_mark,science_mark,social_science_mark,exam_written,total_mark,medium_of_instruction,subject_written,school_name,passing_year,certificate_sl_no,percentage,tenth_board,user_id))

    

    # Login pannina user ID
    

# Next step = HSC
    cursor.execute(
    "UPDATE user SET current_step = %s WHERE id = %s",
    ("hsc", user_id)
)

    db.commit()

    cursor.close()

    return redirect("/hsc")

