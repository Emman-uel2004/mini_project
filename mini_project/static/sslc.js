function validateForm() {

    let subjectLimit = Number(document.getElementsByName("subject_written")[0].value);
    let examLimit = Number(document.getElementsByName("exam_written")[0].value);

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

        if (mark < 0) {
            alert("Marks cannot be less than 0");
            subject.focus();
            return false;
        }

        if (subjectLimit > 0 && mark > subjectLimit) {
            alert("Subject mark cannot be greater than " + subjectLimit);
            subject.focus();
            return false;
        }
    }

    // Total Mark Validation
    let total = Number(document.getElementsByName("total_mark")[0].value);

    if (total > examLimit) {
        alert("Total Mark cannot be greater than " + examLimit);
        document.getElementsByName("total_mark")[0].focus();
        return false;
    }

    return true;
}

// Percentage Calculation
function calculatePercentage() {

    let total = Number(document.getElementsByName("total_mark")[0].value);
    let exam = Number(document.getElementsByName("exam_written")[0].value);

    if (exam > 0) {
        let percentage = (total / exam) * 100;
        document.getElementById("percentage").value = percentage.toFixed(2);
    }
}

document.getElementsByName("total_mark")[0].addEventListener("input", calculatePercentage);
document.getElementsByName("exam_written")[0].addEventListener("change", calculatePercentage);

document.getElementById("sslcForm").addEventListener("submit", function(e) {
    if (!validateForm()) {
        e.preventDefault();
    }
});