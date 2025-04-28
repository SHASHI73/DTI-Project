# Diabetes Detector for Women

## Overview
The **Diabetes Detector for Women** is a *web-based application* designed to provide a preliminary risk assessment for diabetes in women. 
By collecting key health parameters such as **age**, **glucose level**, **blood pressure**, **BMI**, **diabetes pedigree function**, 
**skin thickness**, **insulin level**, and **number of pregnancies**, the system uses a simplified predictive model to estimate the likelihood of diabetes. 
The application is built with **Flask** and **Bootstrap**, offering a user-friendly interface to promote early detection and proactive health management. 

> **Note**: This tool is *not a substitute* for professional medical diagnosis. Users are advised to consult healthcare professionals for accurate assessments.

This project was developed as a capstone project by **Shashi Kumar**  at *Bennett University*, .

diabetes-detector-for-women/
│
├── app.py                  # Main Flask application
├── templates/
│   └── index.html          # HTML template for the web interface
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies

## Features
- **User-Friendly Interface**: A clean, responsive web form built with *Bootstrap* for easy input of health metrics.
- **Health Parameter Input**: Collects critical health data including *age*, *glucose level*, *BMI*, and more.
- **Risk Prediction**: Utilizes a weighted formula to calculate diabetes risk, providing immediate feedback (*high* or *low risk*).
- **Instant Feedback**: Displays clear results with guidance on next steps, emphasizing consultation with healthcare professionals.
- **Data Privacy**: No user data is stored, ensuring basic privacy.
- **Scalable Design**: Modular architecture allows for future enhancements like machine learning integration.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, Bootstrap 5.1.3
- **Libraries**: NumPy (for numerical operations)
- **Development Tools**: 
  - GitHub (code storage)
  - Figma (UI design)
- **Planned Future Stack** (as per project report):
  - JavaScript (Node.js) for backend
  - React.js for frontend
  - MongoDB for database


## Future Enhancements
-Machine Learning: Integrate models like Logistic Regression using Pima Indians Diabetes Database.
-User Profiles: Add authentication for tracking health history.
-Mobile App: Develop using Flutter or React Native.
-Wearable Integration: Use real-time data from devices.
-Education: Offer diet and exercise tips.
-Multilingual Support: Enhance global accessibility.
-Security: Implement GDPR/HIPAA compliance.
 


