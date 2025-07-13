// Initialize coverage chart
function initializeCoverageChart() {
    const ctx = document.getElementById('coverageChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Room Rent', 'Surgery', 'Medicines', 'ICU', 'Diagnostics', 'Other'],
            datasets: [{
                label: 'Covered by Policy',
                data: [42000, 225000, 78000, 62500, 32000, 5000],
                backgroundColor: '#3b82f6',
            }, {
                label: 'Out-of-Pocket',
                data: [8000, 0, 12000, 0, 5000, 115000],
                backgroundColor: '#ef4444',
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    stacked: true,
                    grid: {
                        display: false
                    }
                },
                y: {
                    stacked: true,
                    beginAtZero: true,
                    ticks: {
                        callback: function(value) {
                            return '₹' + value.toLocaleString();
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            let label = context.dataset.label || '';
                            if (label) {
                                label += ': ';
                            }
                            if (context.parsed.y !== null) {
                                label += '₹' + context.parsed.y.toLocaleString();
                            }
                            return label;
                        }
                    }
                }
            }
        }
    });
}

// Initialize research charts
function initializeCharts() {
    initializeCoverageChart();
    
    // Claim settlement chart
    const settlementCtx = document.getElementById('settlementChart').getContext('2d');
    new Chart(settlementCtx, {
        type: 'bar',
        data: {
            labels: ['HealthFirst', 'Star Health', 'HDFC Ergo', 'ICICI Lombard', 'Aditya Birla', 'Industry Avg'],
            datasets: [{
                label: 'Claim Settlement Ratio (%)',
                data: [92.5, 95.2, 89.7, 90.8, 88.3, 91.4],
                backgroundColor: [
                    '#3b82f6',
                    '#64748b',
                    '#64748b',
                    '#64748b',
                    '#64748b',
                    '#10b981'
                ],
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        callback: function(value) {
                            return value + '%';
                        }
                    }
                }
            }
        }
    });
    
    // Complaint statistics chart
    const complaintCtx = document.getElementById('complaintChart').getContext('2d');
    new Chart(complaintCtx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [{
                label: 'HealthFirst Complaints',
                data: [45, 38, 42, 29, 36, 32, 40, 35, 28, 31, 37, 30],
                borderColor: '#3b82f6',
                backgroundColor: 'rgba(59, 130, 246, 0.1)',
                tension: 0.3,
                fill: true
            }, {
                label: 'Industry Average',
                data: [52, 48, 55, 50, 47, 45, 51, 49, 44, 46, 50, 48],
                borderColor: '#64748b',
                borderDash: [5, 5],
                backgroundColor: 'transparent',
                tension: 0.3
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    
    // Rejection reasons chart
    const rejectionCtx = document.getElementById('rejectionChart').getContext('2d');
    new Chart(rejectionCtx, {
        type: 'doughnut',
        data: {
            labels: ['Pre-existing Conditions', 'Policy Lapsed', 'Non-Disclosure', 'Excluded Treatments', 'Document Issues'],
            datasets: [{
                data: [35, 25, 20, 15, 5],
                backgroundColor: [
                    '#ef4444',
                    '#f59e0b',
                    '#3b82f6',
                    '#10b981',
                    '#8b5cf6'
                ]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'right'
                }
            }
        }
    });
    
    // Premium forecast chart
    const premiumCtx = document.getElementById('premiumChart').getContext('2d');
    new Chart(premiumCtx, {
        type: 'line',
        data: {
            labels: ['2023', '2024', '2025', '2026', '2027'],
            datasets: [{
                label: 'Your Policy Premium',
                data: [18500, 20500, 22500, 25000, 27500],
                borderColor: '#3b82f6',
                backgroundColor: 'rgba(59, 130, 246, 0.1)',
                tension: 0.3,
                fill: true
            }, {
                label: 'Industry Average',
                data: [19500, 21000, 22500, 24000, 25500],
                borderColor: '#10b981',
                backgroundColor: 'transparent',
                tension: 0.3
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: false,
                    ticks: {
                        callback: function(value) {
                            return '₹' + value.toLocaleString();
                        }
                    }
                }
            }
        }
    });
}