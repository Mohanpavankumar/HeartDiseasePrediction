# Heart Disease Prediction Web Application

This is a web application for predicting the likelihood of heart disease based on various medical features. The app utilizes machine learning models (SVM, Decision Tree, Logistic Regression, Random Forest, KNN) to provide predictions based on user input.

## Features
- Predict heart disease probability using different classifiers.
- Display individual model predictions and the overall prediction.
- Interactive web interface built using HTML, CSS, and JavaScript.
- Backend powered by Flask, running various machine learning models.
- Fully responsive design.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript (Fetch API)
- **Backend**: Python, Flask
- **Machine Learning Models**: Scikit-learn, joblib
- **Other Libraries**: Numpy, Pandas, Matplotlib (for model analysis)

## Prerequisites
Before running this application, make sure you have the following installed:
- Python 3.x
- Flask
- Scikit-learn
- joblib
- Other dependencies in `requirements.txt`

## Setup Instructions

### 1. Clone the repository
Clone this repository to your local machine.

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run the Flask app
python app.py

<b>Once the Flask server is running, open your browser and go to <a href="http://127.0.0.1:5000/" target="_blank">http://127.0.0.1:5000/</a> to access the heart disease prediction app.</b>


## Example Form Data
Age: 50
Sex: Male
Chest Pain Type: Typical Angina
Resting Blood Pressure: 120 mm Hg
Serum Cholesterol: 240 mg/dl
Fasting Blood Sugar: No
Resting Electrocardiographic Result: Normal
Maximum Heart Rate Achieved: 150 bpm
Exercise Induced Angina: Yes
Oldpeak (ST Depression): 1.5
Slope of Peak Exercise ST Segment: Flat
Number of Major Vessels Colored by Fluoroscopy: 1
Thalassemia: Normal


## Contributing
If you would like to contribute to this project, feel free to submit a pull request. Contributions are welcome for improvements, bug fixes, or new features!

## License
This project is open-source and available under the Kaggle.


