


var ctx = document.getElementById('myChart').getContext('2d');
var ctx = $('#myChart');

var myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['sat', 'sun', 'mon', 'tus', 'wed' ,'thu', 'fri'],
        datasets:[{
            label: 'WEEK',
            data: [8, 9, 10, 7, 8, 9 ,10],
            backgroundColor: 'rgba(0, 200, 200, 0.035)',
            borderColor: 'rgba(0, 200, 200, 1)'

        }]
    },

    options: {
        
        // "fill":false,

        scales: {
            yAxes: [{
                ticks: {
                    min: 0,
                    max: 12,
                    stepSize: 1
                }
            }]
        }
 

    }
});