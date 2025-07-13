import os
import time
import random
from datetime import datetime
from flask import Flask, request, jsonify, render_template

UPLOAD_FOLDER = 'uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create upload directory if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])



def generate_mock_policy_data(filename):
    """Generate mock policy data based on filename"""
    policy_type = 'standard'
    filename = filename.lower()
    
    if 'premium' in filename:
        policy_type = 'premium'
    elif 'basic' in filename:
        policy_type = 'basic'
    
    base_data = {
        "company": "HealthFirst Insurance",
        "policyNumber": f"HF-2024-{random.randint(100000, 999999)}",
        "effectiveDate": datetime.now().strftime("%B %d, %Y"),
        "policyHolder": "John Anderson",
        "sumInsured": "₹7,50,000",
        "features": [
            {
                "name": "Cashless Network",
                "value": "12,500+ hospitals",
                "available": True,
                "hiddenClause": "Only available for planned hospitalizations with prior approval"
            },
            {
                "name": "Pre & Post Hospitalization",
                "value": "60/90 days coverage",
                "available": True
            },
            {
                "name": "Daycare Procedures",
                "value": "550+ procedures covered",
                "available": True
            },
            {
                "name": "Room Rent Limit",
                "value": "₹5,000 per day",
                "available": True,
                "hiddenClause": "Exceeding limit reduces other claim amounts proportionally"
            },
            {
                "name": "Co-payment Clause",
                "value": "15% for treatments > ₹50,000",
                "available": True
            },
            {
                "name": "Restoration Benefit",
                "value": "100% restoration",
                "available": True
            },
            {
                "name": "Annual Health Checkup",
                "value": "₹5,000 per year",
                "available": True
            },
            {
                "name": "Ambulance Cover",
                "value": "₹2,500 per hospitalization",
                "available": True
            },
            {
                "name": "Maternity + Newborn Cover",
                "value": "₹1,00,000" if policy_type != 'premium' else "₹1,50,000",
                "available": True,
                "hiddenClause": "2-year waiting period applies"
            },
            {
                "name": "OPD Benefits",
                "value": "₹10,000" if policy_type != 'premium' else "₹15,000",
                "available": True
            },
            {
                "name": "No Claim Bonus (NCB)",
                "value": "50% bonus",
                "available": True
            },
            {
                "name": "PED Waiting Period",
                "value": "3 years",
                "available": True
            },
            {
                "name": "Disease-wise Sub-limits",
                "value": "Cataract: ₹40,000, Joint: ₹2,00,000" if policy_type != 'premium' else "No sub-limits",
                "available": policy_type == 'premium',
                "hiddenClause": "" if policy_type == 'premium' else "Sub-limits may not cover full treatment costs"
            },
            {
                "name": "Hidden Waiting Periods",
                "value": "None detected",
                "available": True
            }
        ],
        "scenario": {
            "title": "Cardiac Surgery Simulation",
            "description": "Based on your sum insured, here's how your policy would perform for a typical cardiac surgery hospitalization:",
            "costs": [
                {"label": "Total Bill Amount", "value": "₹5,85,000"},
                {"label": "Policy Coverage", "value": "₹4,45,000"},
                {"label": "Co-payment (15%)", "value": "₹67,500"},
                {"label": "Your Payment", "value": "₹1,40,000"}
            ]
        },
        "gaps": [
            {
                "icon": "fa-bed",
                "title": "Room Rent Limit Below Average",
                "description": "Your ₹5,000/day limit is below the average private room cost of ₹7,500 in metro cities. This may lead to proportional deductions on other expenses.",
                "recommendation": "Consider upgrading to a plan with ₹7,500+ room rent coverage to avoid deductions."
            },
            {
                "icon": "fa-briefcase-medical",
                "title": "Limited Pre-existing Conditions Coverage",
                "description": "Coverage for pre-existing conditions begins only after 3 years of continuous policy renewal.",
                "recommendation": "Explore policies with 1-2 year waiting periods for better coverage."
            },
            {
                "icon": "fa-file-medical",
                "title": "Mental Health Coverage Limitations" if policy_type != 'premium' else "Alternative Treatment Limitations",
                "description": "Mental health treatments limited to ₹50,000/year" if policy_type != 'premium' else "Ayurveda and Homeopathy treatments limited to ₹50,000/year",
                "recommendation": "Look for policies with comprehensive mental health coverage." if policy_type != 'premium' else "Look for policies with higher alternative treatment coverage."
            }
        ],
        "aiAnalysis": [
            "The room rent limit clause contains a proportional deduction clause that could significantly reduce coverage for other expenses if a higher-cost room is used.",
            "The maternity cover has a 2-year waiting period that begins from policy inception, not from the start of pregnancy.",
            "The co-payment clause applies to all treatments above ₹50,000, including diagnostics and medicines."
        ],
        "stats": {
            "featuresPassed": 11 if policy_type == 'standard' else 13 if policy_type == 'premium' else 9,
            "coverageGaps": 3 if policy_type == 'standard' else 1 if policy_type == 'premium' else 5,
            "sumInsured": "₹7.5L" if policy_type == 'standard' else "₹10L" if policy_type == 'premium' else "₹5L"
        }
    }
    
    # Adjust sum insured based on policy type
    if policy_type == 'premium':
        base_data["sumInsured"] = "₹10,00,000"
    elif policy_type == 'basic':
        base_data["sumInsured"] = "₹5,00,000"
    
    return base_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_policy():
    """Endpoint to handle policy analysis"""
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Check allowed extensions
    allowed_extensions = {'pdf', 'jpg', 'jpeg', 'png'}
    if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
        return jsonify({"error": "Invalid file type. Supported: PDF, JPG, PNG"}), 400
    
    # Save file temporarily (in real app, process it here)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    
    # Simulate processing delay
    time.sleep(2)
    
    # Generate mock response based on filename
    policy_data = generate_mock_policy_data(file.filename)
    
    # Clean up: remove the file after processing
    try:
        os.remove(filepath)
    except Exception as e:
        print(f"Error removing file: {e}")
    
    return jsonify(policy_data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)