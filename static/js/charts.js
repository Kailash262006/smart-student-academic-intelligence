const performanceCtx = document.getElementById('performanceChart');

if (performanceCtx) {
  new Chart(performanceCtx, {
    type: 'bar',
    data: {
      labels: subjectLabels, // from Flask
      datasets: [{
        label: 'Performance (%)',
        data: subjectScores,
        backgroundColor: [
          '#FF7043', // Coral Orange
          '#1E88E5', // Tropical Blue
          '#43A047', // Leaf Green
          '#FDD835', // Sunshine Yellow
          '#8E24AA'  // Purple accent
        ],
        borderRadius: 12,
        borderSkipped: false
      }]
    },
    options: {
      responsive: true,
      animation: {
        duration: 1200,
        easing: 'easeOutBounce'
      },
      plugins: {
        legend: {
          display: false
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          ticks: {
            color: '#444',
            callback: value => value + '%'
          },
          grid: {
            color: '#eaeaea'
          }
        },
        x: {
          ticks: {
            color: '#444'
          },
          grid: {
            display: false
          }
        }
      }
    }
  });
}
const focusCtx = document.getElementById('focusChart');

if (focusCtx) {
  new Chart(focusCtx, {
    type: 'doughnut',
    data: {
      labels: ['Focused Time', 'Distracted Time'],
      datasets: [{
        data: [focusPercent, distractionPercent],
        backgroundColor: [
          '#43A047', // Green = focus
          '#FF7043'  // Orange = distraction
        ],
        hoverOffset: 12
      }]
    },
    options: {
      cutout: '70%',
      animation: {
        animateRotate: true,
        duration: 1200
      },
      plugins: {
        legend: {
          position: 'bottom',
          labels: {
            color: '#333',
            font: {
              size: 14,
              weight: '600'
            }
          }
        },
        tooltip: {
          callbacks: {
            label: context => context.label + ': ' + context.raw + '%'
          }
        }
      }
    }
  });
}
