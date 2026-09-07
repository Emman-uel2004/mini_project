function validateForm() {

    let subjectLimit = Number(
        document.getElementsByName("subject_written")[0].value
    );

    let examLimit = Number(
        document.getElementsByName("exam_written")[0].value
    );

    let subjects = [
        document.getElementsByName("language1_mark")[0],
        document.getElementsByName("language2_mark")[0],
        document.getElementsByName("mathematics_mark")[0],
        document.getElementsByName("science_mark")[0],
        document.getElementsByName("social_science_mark")[0]
    ];

    // Subject Marks Validation
    for (let subject of subjects) {

        let mark = Number(subject.value);

        // Negative mark
        if (mark < 0) {
            alert("Marks cannot be less than 0");
            subject.focus();
            return false;
        }

        // Subject mark limit
        if (subjectLimit > 0 && mark > subjectLimit) {
            alert("Subject mark cannot be greater than " + subjectLimit);
            subject.focus();
            return false;
        }
    }

    // Exam Written must be selected
    if (examLimit <= 0) {
        alert("Please select Exam Written");
        document.getElementsByName("exam_written")[0].focus();
        return false;
    }

    // Calculate total from 5 subjects
    let total = 0;

    for (let subject of subjects) {
        total += Number(subject.value);
    }

    // Set total mark
    document.getElementsByName("total_mark")[0].value = total;

    // Total cannot exceed exam limit
    if (total > examLimit) {
        alert("Total Mark cannot be greater than " + examLimit);
        document.getElementsByName("total_mark")[0].focus();
        return false;
    }

    // Calculate percentage
    let percentage = (total / examLimit) * 100;

    document.getElementById("percentage").value =
        percentage.toFixed(2);

    return true;
}


// Percentage Calculation
function calculatePercentage() {

    let subjects = [
        document.getElementsByName("language1_mark")[0],
        document.getElementsByName("language2_mark")[0],
        document.getElementsByName("mathematics_mark")[0],
        document.getElementsByName("science_mark")[0],
        document.getElementsByName("social_science_mark")[0]
    ];

    let exam = Number(
        document.getElementsByName("exam_written")[0].value
    );

    // Add all 5 subjects
    let total = 0;

    for (let subject of subjects) {
        total += Number(subject.value) || 0;
    }

    // Display total
    document.getElementsByName("total_mark")[0].value = total;

    // Calculate percentage
    if (exam > 0) {

        let percentage = (total / exam) * 100;

        document.getElementById("percentage").value =
            percentage.toFixed(2);
    } else {

        document.getElementById("percentage").value = "";
    }
}


// Get all 5 subject inputs
let subjects = [
    document.getElementsByName("language1_mark")[0],
    document.getElementsByName("language2_mark")[0],
    document.getElementsByName("mathematics_mark")[0],
    document.getElementsByName("science_mark")[0],
    document.getElementsByName("social_science_mark")[0]
];


// When subject mark changes
for (let subject of subjects) {
    subject.addEventListener("input", calculatePercentage);
}


// When Exam Written changes
document
    .getElementsByName("exam_written")[0]
    .addEventListener("change", calculatePercentage);


// Form Submit
document.getElementById("sslcForm").addEventListener("submit", function(e) {

    if (!validateForm()) {
        e.preventDefault();
    }

});