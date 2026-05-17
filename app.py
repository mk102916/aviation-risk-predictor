import streamlit as st
import pandas as pd
import joblib
import datetime

# Load model
model = joblib.load('aviation_risk_model.pkl')
le = joblib.load('label_encoder.pkl')

features = ['Month', 'DayofMonth', 'DayOfWeek', 'CRSDepTime', 'Carrier_Code']

st.title("✈ Aviation Risk Predictor")

year = st.number_input("Year", 1987, 2030, 2025)
month = st.number_input("Month", 1, 12, 1)
day = st.number_input("Day", 1, 31, 1)
time = st.number_input("Departure Time", 0, 2359, 1430)

carrier = st.text_input("Carrier Code", "AA")

if st.button("Predict"):

    dt = datetime.date(year, month, day)
    day_of_week = dt.isoweekday()

    try:
        carrier_encoded = le.transform([carrier])[0]
    except:
        carrier_encoded = 0

    input_values = [[month, day, day_of_week, time, carrier_encoded]]

    new_data = pd.DataFrame(input_values, columns=features)

    prediction = model.predict(new_data)[0]
    probability = model.predict_proba(new_data)[0][1]

    if prediction == 1:
        st.error(f"HIGH RISK ({probability*100:.1f}%)")
    else:
        st.success(f"LOW RISK ({(1-probability)*100:.1f}% Safe)")