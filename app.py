from Flask import Flask, render_template, request
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Create the templates directory and add this HTML file
with open('templates/index.html', 'w') as f:
    f.write('''
<!DOCTYPE html>
<html>
<head>
    <title>Diabetes Risk Assessment</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { 
            padding: 20px;
            background-color: #f8f9fa;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            border-radius: 5px;
        }
        .high-risk {
            background-color: #f8d7da;
            border: 1px solid #f5c6cb;
        }
        .low-risk {
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2 class="mb-4 text-center">Diabetes Risk Assessment</h2>
        <form method="POST">
            <div class="row">
                <div class="col-md-6">
                    <div class="form-group">
                        <label>Age (years)</label>
                        <input type="number" class="form-control" name="age" required min="0" max="120">
                    </div>
                    <div class="form-group">
                        <label>Glucose Level (mg/dL)</label>
                        <input type="number" class="form-control" name="glucose" required min="0" max="500">
                    </div>
                    <div class="form-group">
                        <label>Blood Pressure (mm Hg)</label>
                        <input type="number" class="form-control" name="blood_pressure" required min="0" max="300">
                    </div>
                    <div class="form-group">
                        <label>BMI</label>
                        <input type="number" step="0.1" class="form-control" name="bmi" required min="0" max="100">
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="form-group">
                        <label>Diabetes Pedigree Function</label>
                        <input type="number" step="0.01" class="form-control" name="diabetes_pedigree" required min="0" max="10">
                    </div>
                    <div class="form-group">
                        <label>Skin Thickness (mm)</label>
                        <input type="number" class="form-control" name="skin_thickness" required min="0" max="100">
                    </div>
                    <div class="form-group">
                        <label>Insulin (mu U/ml)</label>
                        <input type="number" class="form-control" name="insulin" required min="0" max="1000">
                    </div>
                    <div class="form-group">
                        <label>Pregnancies (number)</label>
                        <input type="number" class="form-control" name="pregnancies" required min="0" max="20">
                    </div>
                </div>
            </div>
            <div class="text-center">
                <button type="submit" class="btn btn-primary mt-3">Check Risk</button>
            </div>
        </form>
        
        {% if prediction is defined %}
        <div class="result {% if prediction == 1 %}high-risk{% else %}low-risk{% endif %}">
            <h4 class="text-center">
                {% if prediction == 1 %}
                    Higher risk of diabetes detected. Please consult a healthcare professional.
                {% else %}
                    Lower risk of diabetes detected. However, maintain a healthy lifestyle.
                {% endif %}
            </h4>
            <p class="text-center">
                <small>This is not a medical diagnosis. Always consult healthcare professionals for proper medical advice.</small>
            </p>
        </div>
        {% endif %}
    </div>
</body>
</html>
    ''')

def predict_diabetes(features):
    # This is a simplified prediction model for demonstration
    # In a real application, you would use a properly trained model
    glucose_weight = 0.0028
    bmi_weight = 0.0173
    age_weight = 0.0183
    bp_weight = 0.0008
    dp_weight = 0.4474
    
    # Calculate risk score
    risk_score = (
        features[0] * glucose_weight +
        features[1] * bmi_weight +
        features[2] * age_weight +
        features[3] * bp_weight +
        features[4] * dp_weight
    )
    
    # Return 1 for high risk, 0 for low risk
    return 1 if risk_score > 0.5 else 0

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Get values from the form
        features = [
            float(request.form['glucose']),
            float(request.form['bmi']),
            float(request.form['age']),
            float(request.form['blood_pressure']),
            float(request.form['diabetes_pedigree']),
            float(request.form['skin_thickness']),
            float(request.form['insulin']),
            float(request.form['pregnancies'])
        ]
        
        # Make prediction
        prediction = predict_diabetes(features)
    
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)