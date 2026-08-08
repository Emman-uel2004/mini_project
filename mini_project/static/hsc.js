
const group = document.getElementById("group");

const subjects = document.getElementById("subjects");

const totalInput = document.getElementById("total");

const percentageInput =
    document.getElementById("percentage");


// Subject Written

const subjectWritten =
    document.querySelector(
        'select[name="subject_written"]'
    );


// Exam Written

const examWritten =
    document.querySelector(
        'select[name="exam_written"]'
    );


// Group change

group.addEventListener("change", function () {

    const selectedGroup = this.value;

    let subjectList = [];


    if (selectedGroup === "Computer Science") {

        subjectList = [
            "Tamil",
            "English",
            "Mathematics",
            "Physics",
            "Chemistry",
            "Computer Science"
        ];

    }


    else if (selectedGroup === "Biology") {

        subjectList = [
            "Tamil",
            "English",
            "Mathematics",
            "Physics",
            "Chemistry",
            "Biology"
        ];

    }


    else if (selectedGroup === "Commerce") {

        subjectList = [
            "Tamil",
            "English",
            "Accountancy",
            "Commerce",
            "Economics",
            "Computer Applications"
        ];

    }


    else if (selectedGroup === "Arts") {

        subjectList = [
            "Tamil",
            "English",
            "History",
            "Economics",
            "Political Science",
            "Geography"
        ];

    }


    subjects.innerHTML =
        "<h3>Subjects & Marks</h3>";


    subjectList.forEach(function (subject) {

        const name = subject
            .toLowerCase()
            .replaceAll(" ", "_");


        subjects.innerHTML += `

            <div class="subject">

                <label>${subject}</label>

                <input
                    type="number"
                    name="${name}"
                    class="mark"
                    min="0"
                    placeholder="Enter Mark"
                    required
                >

            </div>

        `;

    });


    updateMarkLimit();

    calculateMarks();

});


// Subject Written change

subjectWritten.addEventListener(
    "change",
    function () {

        updateMarkLimit();

        calculateMarks();

    }
);


// Exam Written change

examWritten.addEventListener(
    "change",
    function () {

        calculateMarks();

    }
);


// Set maximum mark for every subject

function updateMarkLimit() {

    const maxMark =
        Number(subjectWritten.value);


    const markInputs =
        document.querySelectorAll(".mark");


    markInputs.forEach(function (input) {

        if (maxMark > 0) {

            input.max = maxMark;

            input.placeholder =
                "Enter Mark (0 - " + maxMark + ")";

        }

    });

}


// Mark input

document.addEventListener(
    "input",
    function (event) {

        if (
            event.target.classList.contains("mark")
        ) {

            const maxMark =
                Number(subjectWritten.value);


            const currentMark =
                Number(event.target.value);


            if (
                maxMark > 0 &&
                currentMark > maxMark
            ) {

                alert(
                    "Mark cannot be greater than "
                    + maxMark
                );

                event.target.value = maxMark;

            }


            if (currentMark < 0) {

                event.target.value = 0;

            }


            calculateMarks();

        }

    }
);


// Calculate total and percentage

function calculateMarks() {

    const marks =
        document.querySelectorAll(".mark");


    let total = 0;

    let count = 0;


    marks.forEach(function (input) {

        if (input.value !== "") {

            total += Number(input.value);

            count++;

        }

    });


    // Exam Written maximum

    const examMaximum =
        Number(examWritten.value);


    // Check total

    if (
        examMaximum > 0 &&
        total > examMaximum
    ) {

        alert(
            "Total mark cannot be greater than "
            + examMaximum
        );

        totalInput.value = total;

    }

    else {

        totalInput.value = total;

    }


    // Percentage

    if (count > 0) {

        const percentage =
            total / count;


        percentageInput.value =
            percentage.toFixed(2);

    }

    else {

        percentageInput.value = "";

    }

}

