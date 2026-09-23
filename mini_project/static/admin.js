// Get dashboard data from Flask

const data = window.dashboardData;


// =====================================
// 1. GENDER DISTRIBUTION
// =====================================

const genderLabels = data.gender.map(item => item.gender);

const genderValues = data.gender.map(item => item.count);


Plotly.newPlot(
    "genderChart",

    [
        {
            labels: genderLabels,
            values: genderValues,
            type: "pie",
            hole: 0.35
        }
    ],

    {
        title: "Gender Distribution"
    }
);


// =====================================
// 2. ADMISSION TYPE
// =====================================

const admissionLabels =
    data.admission.map(item => item.admission_type);

const admissionValues =
    data.admission.map(item => item.count);


Plotly.newPlot(
    "admissionChart",

    [
        {
            labels: admissionLabels,
            values: admissionValues,
            type: "pie",
            hole: 0.35
        }
    ],

    {
        title: "Admission Type"
    }
);


// =====================================
// 3. ACADEMIC AVERAGE
// =====================================

Plotly.newPlot(
    "averageChart",

    [
        {
            x: ["SSLC", "HSC", "UG"],

            y: [
                data.sslc_average,
                data.hsc_average,
                data.ug_average
            ],

            type: "bar"
        }
    ],

    {
        title: "Academic Average",

        yaxis: {
            title: "Percentage"
        }
    }
);

// =====================================
// 4. SSLC PASSING YEAR
// =====================================

const passingYearLabels =
    data.passing_year.map(item => item.passing_year);

const passingYearValues =
    data.passing_year.map(item => item.count);


Plotly.newPlot(
    "passingYearChart",

    [
        {
            x: passingYearLabels,
            y: passingYearValues,
            type: "bar"
        }
    ],

    {
        title: "SSLC Passing Year",

        xaxis: {
            title: "Passing Year"
        },

        yaxis: {
            title: "Number of Students"
        }
    }
);