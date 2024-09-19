// Get the data passed from Flask
var times = {{ times | tojson }};
var trafficSituations = {{ traffic_situations | tojson }};

// Map traffic situations to colors for visualization
var trafficColors = trafficSituations.map(function(situation) {
    if (situation === 'High') return 'rgba(255, 99, 132, 0.7)';
    else if (situation === 'Medium') return 'rgba(255, 206, 86, 0.7)';
    else if (situation === 'Low') return 'rgba(75, 192, 192, 0.7)';
    else return 'rgba(153, 102, 255, 0.7)';  // Default color for unknown situations
});

// Create the chart using Chart.js
var ctx = document.getElementById('trafficChart').getContext('2d');
var trafficChart = new Chart(ctx, {
    type: 'bar',  // You can change this to 'line', 'pie', etc.
    data: {
        labels: times,  // X-axis labels (Time)
        datasets: [{
            label: 'Traffic Situation',
            data: trafficSituations.map(situation => {
                if (situation === 'High') return 3;
                else if (situation === 'Medium') return 2;
                else if (situation === 'Low') return 1;
                return 0; // Default for unknown situations
            }),  // Y-axis values (numerical representation)
            backgroundColor: trafficColors,  // Colors based on traffic situation
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,  // Make the chart responsive
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    stepSize: 1,
                    callback: function(value) {
                        if (value === 1) return 'Low';
                        if (value === 2) return 'Medium';
                        if (value === 3) return 'High';
                        return '';
                    }
                }
            }
        }
    }
});