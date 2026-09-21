import mysql.connector
from werkzeug.security import generate_password_hash
from datetime import date, timedelta


# ==========================================
# MYSQL CONNECTION
# ==========================================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",
    database="login_db"
)

cursor = db.cursor()


# ==========================================
# DATA
# ==========================================

first_names = [
    "Arun", "Ajay", "Akash", "Bala", "Bharath",
    "Dinesh", "Dharshan", "Deepak", "Gokul", "Hari",
    "Harish", "Karthik", "Kavin", "Manoj", "Mohan",
    "Naveen", "Prakash", "Praveen", "Rahul", "Raj",
    "Ravi", "Rohit", "Sanjay", "Saravanan", "Sathish",
    "Surya", "Vignesh", "Vijay", "Vimal", "Vishnu",
    "Yogesh", "Abinash", "Abhishek", "Adithya", "Ajith",
    "Anand", "Anbu", "Ashwin", "Balaji", "Chandru",
    "Dhanush", "Ganesh", "Gowtham", "Jeeva", "Kamal",
    "Lokesh", "Madhan", "Mahesh", "Mukesh", "Nithin"
]

last_names = [
    "Kumar",
    "Raj",
    "Joseph",
    "Prasad"
]


blood_groups = [
    "A+",
    "A-",
    "B+",
    "B-",
    "O+",
    "O-"
]

admission_types = [
    "Government",
    "Management"
]

mother_tongues = [
    "Tamil",
    "English"
]

nationalities = [
    "india",
    "usa",
    "canada",
    "africa",
    "barginofao",
    "nigeriya"
]

genders = [
    "male",
    "femal",
    "others"
]

castes = [
    "OC",
    "BC",
    "MBC",
    "SC",
    "ST"
]

mediums = [
    "Tamil",
    "English"
]

sslc_boards = [
    "State_Board",
    "CBSE"
]

hsc_groups = [
    "Computer Science",
    "Biology",
    "Commerce",
    "Arts"
]

hsc_boards = [
    "Tamil Nadu State Board",
    "CBSE",
    "ICSE",
    "Other"
]

ug_degrees = [
    "B.Sc Computer Science",
    "BCom.",
    "BCA",
    "BBA",
    "B.E",
    "B.Tech"
]

universities = [
    "Pondicherry University",
    "University of Madras",
    "Bharathiar University"
]


# ==========================================
# GENERATE 200 UNIQUE NAMES
# ==========================================

unique_names = []

for first in first_names:
    for last in last_names:

        name = first + " " + last

        if name not in unique_names:
            unique_names.append(name)

        if len(unique_names) == 200:
            break

    if len(unique_names) == 200:
        break


# ==========================================
# PASSWORD
# ==========================================

password = "Student@123"

hashed_password = generate_password_hash(password)


# ==========================================
# INSERT 200 STUDENTS
# ==========================================

for i in range(1, 201):

    username = f"student{i}"

    fullname = unique_names[i - 1]

    email = f"student{i}@gmail.com"


    # ======================================
    # USER TABLE
    # ======================================

    cursor.execute(
        """
        INSERT INTO user
        (
            username,
            password,
            fullname,
            email,
            current_step
        )
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            username,
            hashed_password,
            fullname,
            email,
            "completed"
        )
    )

    user_id = cursor.lastrowid


    # ======================================
    # PERSONAL DETAILS
    # ======================================

    initial = fullname[0]

    first_name = fullname.split()[0]

    father_name = first_name + " Father"

    mother_name = first_name + " Mother"

    blood_group = blood_groups[(i - 1) % len(blood_groups)]

    admission_type = admission_types[(i - 1) % 2]

    contact = f"{9000000000 + i}"

    mother_tongue = mother_tongues[(i - 1) % 2]

    dob = date(2000, 1, 1) + timedelta(days=i * 5)

    caste = castes[(i - 1) % len(castes)]

    aadhar = f"{100000000000 + i}"

    nationality = nationalities[(i - 1) % len(nationalities)]

    gender = genders[(i - 1) % len(genders)]


    # ======================================
    # INTENTIONAL PERSONAL DATA MISTAKES
    # ======================================

    # Student 15 → duplicate contact
    if i == 15:
        contact = "9000000001"

    # Student 25 → invalid email
    if i == 25:
        email = "student25@gmail"

    # Student 35 → duplicate Aadhaar
    if i == 35:
        aadhar = "100000000010"

    # Student 45 → invalid blood group
    if i == 45:
        blood_group = "AB+"

    # Student 55 → inconsistent nationality
    if i == 55:
        nationality = "India"


    cursor.execute(
        """
        INSERT INTO persnol
        (
            user_id,
            name,
            initial,
            father_name,
            mother_name,
            blood_group,
            admission_type,
            contact,
            mother_tongue,
            dob,
            cast,
            aadhar,
            nationality,
            email,
            gender
        )
        VALUES
        (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s
        )
        """,
        (
            user_id,
            fullname,
            initial,
            father_name,
            mother_name,
            blood_group,
            admission_type,
            contact,
            mother_tongue,
            dob,
            caste,
            aadhar,
            nationality,
            email,
            gender
        )
    )


    # ======================================
    # SSLC
    # ======================================

    language1 = 70 + (i % 20)
    language2 = 68 + (i % 20)
    mathematics = 72 + (i % 20)
    science = 70 + (i % 20)
    social_science = 73 + (i % 20)

    total_mark = (
        language1 +
        language2 +
        mathematics +
        science +
        social_science
    )

    percentage = round(total_mark / 5, 2)

    subject_written_options = [
        "100",
        "200",
        "300",
        "400"
    ]

    exam_written_options = [
        "500",
        "600",
        "700",
        "800"
    ]

    subject_written = subject_written_options[(i - 1) % 4]

    exam_written = exam_written_options[(i - 1) % 4]

    medium = mediums[(i - 1) % 2]

    school_names = [
        "Government Higher Secondary School",
        "Sri Vidya Matriculation Higher Secondary School",
        "St. Mary's Higher Secondary School"
    ]

    school_name = (
        school_names[(i - 1) % 3]
        + f" {i}"
    )

    passing_year = 2018 + ((i - 1) % 5)

    certificate_sl_no = f"SSLC{i:04d}"

    tenth_board = sslc_boards[(i - 1) % 2]


    # ======================================
    # SSLC INTENTIONAL MISTAKES
    # ======================================

    # Student 10 → percentage greater than 100
    if i == 10:
        percentage = 105

    # Student 20 → negative mark
    if i == 20:
        mathematics = -10

    # Student 30 → invalid board
    if i == 30:
        tenth_board = "STATE"

    # Student 40 → future passing year
    if i == 40:
        passing_year = 2035

    # Student 50 → duplicate certificate
    if i == 50:
        certificate_sl_no = "SSLC0001"


    cursor.execute(
        """
        INSERT INTO sslc
        (
            language1_mark,
            language2_mark,
            mathematics_mark,
            science_mark,
            social_science_mark,
            exam_written,
            total_mark,
            medium_of_instruction,
            school_name,
            passing_year,
            certificate_sl_no,
            subject_written,
            percentage,
            tenth_board,
            user_id
        )
        VALUES
        (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s
        )
        """,
        (
            language1,
            language2,
            mathematics,
            science,
            social_science,
            exam_written,
            total_mark,
            medium,
            school_name,
            passing_year,
            certificate_sl_no,
            subject_written,
            percentage,
            tenth_board,
            user_id
        )
    )


    # ======================================
    # HSC
    # ======================================

    tamil = 75 + (i % 15)
    english = 70 + (i % 15)
    mathematics_hsc = 65 + (i % 15)
    physics = 60 + (i % 15)
    chemistry = 62 + (i % 15)
    computer_science = 70 + (i % 15)

    total = (
        tamil +
        english +
        mathematics_hsc +
        physics +
        chemistry +
        computer_science
    )

    hsc_percentage = round(total / 6, 2)

    board = hsc_boards[(i - 1) % 4]

    group_name = hsc_groups[(i - 1) % 4]

    exam_written_hsc = exam_written_options[(i - 1) % 4]

    subject_written_hsc = subject_written_options[(i - 1) % 4]

    hsc_medium = mediums[(i - 1) % 2]

    hsc_school = (
        school_names[(i - 1) % 3]
        + f" {i}"
    )

    hsc_passing_year = 2020 + ((i - 1) % 5)

    hsc_certificate = f"HSC{i:04d}"


    # Other subjects NULL
    biology = None
    accountancy = None
    commerce = None
    economics = None
    computer_applications = None
    history = None
    political_science = None
    geography = None


    # ======================================
    # HSC INTENTIONAL MISTAKES
    # ======================================

    # Student 60 → percentage > 100
    if i == 60:
        hsc_percentage = 110

    # Student 70 → wrong total
    if i == 70:
        total = 600

    # Student 80 → invalid group
    if i == 80:
        group_name = "Bio-Maths"

    # Student 90 → future passing year
    if i == 90:
        hsc_passing_year = 2036

    # Student 100 → duplicate HSC certificate
    if i == 100:
        hsc_certificate = "HSC0001"


    cursor.execute(
        """
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
            certificate_sl_no,
            user_id
        )
        VALUES
        (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s
        )
        """,
        (
            board,
            group_name,
            tamil,
            english,
            mathematics_hsc,
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
            hsc_percentage,
            exam_written_hsc,
            subject_written_hsc,
            hsc_medium,
            hsc_school,
            hsc_passing_year,
            hsc_certificate,
            user_id
        )
    )


    # ======================================
    # UG
    # ======================================

    ug_degree = ug_degrees[(i - 1) % len(ug_degrees)]

    ug_percentage = round(
        60 + ((i - 1) % 30) * 0.5,
        2
    )

    consolidated_certificate = f"CONS{i:03d}"

    provisional_certificate = f"PROV{i:03d}"

    if ug_percentage >= 60:
        ug_class = "First Class"
    elif ug_percentage >= 50:
        ug_class = "Second Class"
    else:
        ug_class = "Third Class"

    college_names = [
        "Government Arts and Science College",
        "Sri Ram College of Arts and Science",
        "St. Joseph College"
    ]

    ug_college = (
        college_names[(i - 1) % 3]
        + f" {i}"
    )

    university = universities[(i - 1) % 3]

    year_of_passing = 2023 + ((i - 1) % 4)


    # ======================================
    # UG INTENTIONAL MISTAKES
    # ======================================

    # Student 110 → negative percentage
    if i == 110:
        ug_percentage = -5

    # Student 120 → percentage > 100
    if i == 120:
        ug_percentage = 105

    # Student 130 → invalid degree
    if i == 130:
        ug_degree = "MCA Computer Science"

    # Student 140 → future passing year
    if i == 140:
        year_of_passing = 2037

    # Student 150 → duplicate provisional certificate
    if i == 150:
        provisional_certificate = "PROV001"


    cursor.execute(
        """
        INSERT INTO ug
        (
            ug_degree,
            ug_percentage,
            consolidated_certificate,
            provisional_certificate,
            ug_class,
            ug_college,
            university,
            year_of_passing,
            user_id
        )
        VALUES
        (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s
        )
        """,
        (
            ug_degree,
            ug_percentage,
            consolidated_certificate,
            provisional_certificate,
            ug_class,
            ug_college,
            university,
            year_of_passing,
            user_id
        )
    )


    print(
        f"Student {i} inserted | "
        f"{username} | "
        f"{fullname} | "
        f"User ID: {user_id}"
    )


# ==========================================
# COMMIT
# ==========================================

db.commit()

cursor.close()
db.close()


print()
print("==========================================")
print("200 STUDENTS INSERTED SUCCESSFULLY")
print("==========================================")
print("Password               : Student@123")
print("Username               : student1 - student200")
print("Provisional Certificate: PROV001 - PROV200")
print("Consolidated Certificate: CONS001 - CONS200")
print("==========================================")
print("Intentional mistakes are also included.")
print("Use Pandas / SQL to find and clean them.")
print("==========================================")