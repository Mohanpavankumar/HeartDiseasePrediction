from flask import Flask, request, jsonify, send_from_directory
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the trained models
svm_model = joblib.load('svm_model.pkl')
dt_model = joblib.load('dt_model.pkl')
lr_model = joblib.load('lr_model.pkl')
rf_model = joblib.load('rf_model.pkl')
knn_classifier = joblib.load('knn_classifier.pkl')
# fnn_model = joblib.load('fnn_model.pkl')
# mlp_model = joblib.load('mlp_model.pkl')
# dnn_model = joblib.load('dnn_model.pkl')

# Route for the root URL
@app.route('/')
def index():
    return 'Welcome to the Heart Disease Prediction Model! Please visit /index to access the form.'

# Route to serve the HTML page (index.html)
@app.route('/index')
def serve_index():
    return send_from_directory('templates', 'index.html')  # Make sure your HTML is in the 'templates' folder

# Route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the POST request (ensure it's in JSON format)
        data = request.get_json()

        # Convert the data into a numpy array suitable for the models
        features = np.array([[
            int(data['age']),               # Age
            int(data['sex']),               # Sex (0 or 1)
            int(data['cp']),                # Chest Pain Type
            int(data['trestbps']),          # Resting Blood Pressure
            int(data['chol']),              # Serum Cholesterol
            int(data['fbs']),               # Fasting Blood Sugar
            int(data['restecg']),           # Resting Electrocardiographic Result
            int(data['thalach']),           # Maximum Heart Rate Achieved
            int(data['exang']),             # Exercise Induced Angina
            float(data['oldpeak']),         # Oldpeak (ST depression)
            int(data['slope']),             # Slope of Peak Exercise ST Segment
            int(data['ca']),                # Number of Major Vessels Colored by Fluoroscopy
            int(data['thal'])               # Thalassemia
        ]])

        # Make predictions with each model
        svm_prediction = svm_model.predict(features)[0]
        dt_prediction = dt_model.predict(features)[0]
        lr_prediction = lr_model.predict(features)[0]
        rf_prediction = rf_model.predict(features)[0]
        knn_classifier = rf_model.predict(features)[0]
#       fnn_pred = fnn_model.predict(features)[0]
#       mlp_pred = mlp_model.predict(features)[0]

# Collect individual predictions in a list
        predictions = [
            svm_prediction, dt_prediction, lr_prediction, rf_prediction, knn_classifier
        ]
        
        # Calculate the probability of heart disease as the percentage of models that predicted '1'
        heart_disease_probability = (sum(predictions) / len(predictions)) * 100

        # Return the predictions as a JSON response
        return jsonify({
            'svm_prediction': int(svm_prediction),
            'dt_prediction': int(dt_prediction),
            'lr_prediction': int(lr_prediction),
            'rf_prediction': int(rf_prediction),
            'knn_classifier': int(knn_classifier),
            'heart_disease_probability': f"{heart_disease_probability:.2f}%"
#           'FNN Prediction': int(fnn_pred),
#           'MLP Prediction': int(mlp_pred),
#           'DNN Prediction': int(dnn_pred)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Send an error response with status 400

if __name__ == '__main__':
    # Run the app
    app.run(debug=True)

