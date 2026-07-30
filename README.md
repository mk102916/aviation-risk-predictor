# Aviation-Risk-Predictor
Machine Learning-based aviation safety risk prediction system using Python, Streamlit, and Decision Tree Classification.

---

## Overview

The Aviation Safety Risk Prediction System is a machine learning web application that predicts whether a flight has a **Low Risk** or **High Risk** safety profile based on historical flight information. The project uses a Decision Tree Classifier trained on aviation data and provides real-time predictions through a Streamlit web interface.

---

## Features

* Predicts aviation safety risk using historical flight data.
* Interactive Streamlit web application.
* Machine learning model built using Decision Tree Classification.
* Automatic calculation of the day of the week from the selected date.
* Displays prediction along with confidence score.
* Data visualization using confusion matrix and decision tree.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Matplotlib
* Seaborn
* Joblib

---

## Dataset

The model is trained on a combined aviation dataset containing historical flight information such as:

* Month
* Day of Month
* Day of Week
* Scheduled Departure Time
* Airline Carrier
* Flight Delays
* Cancellation Status

A safety risk label is created based on:

* Flight cancellation
* Weather delays greater than 15 minutes

---

## How It Works

1. Enter:

   * Year
   * Month
   * Day
   * Scheduled Departure Time
   * Airline Carrier Code
2. Click **Predict**.
3. The model predicts whether the flight is **Low Risk** or **High Risk** and displays the confidence score.

---

## Future Improvements

* Random Forest and XGBoost models for improved accuracy.
* Live weather integration.
* Airport location support.
* Interactive analytics dashboard.
* Flight delay visualization.
* Cloud deployment on AWS.
* Explainable AI (SHAP/LIME) for prediction insights.

---

## Author

**Mihita Karwale**

B.Tech – Information Technology & Data Science


