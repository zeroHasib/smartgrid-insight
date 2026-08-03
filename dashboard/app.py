import streamlit as st
import joblib
import pandas as pd
from pathlib import Path


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="SmartGrid Insight",
    page_icon="⚡",
    layout="wide"
)


# ==========================================
# Load Trained Model
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "energy_model.pkl"

model = joblib.load(MODEL_PATH)


# ==========================================
# Sidebar
# ==========================================

st.sidebar.header("Project Information")

st.sidebar.info("""
Model: Linear Regression

MAE: 4.09

R² Score: 0.593
""")


# ==========================================
# Main Title
# ==========================================

st.title("⚡ SmartGrid Insight")
st.subheader("Energy Consumption Forecasting System")


# ==========================================
# User Inputs
# ==========================================

temperature = st.number_input(
    "Temperature",
    value=25.0
)

humidity = st.number_input(
    "Humidity",
    value=50.0
)

square_footage = st.number_input(
    "Square Footage",
    value=2000.0
)

occupancy = st.number_input(
    "Occupancy",
    value=4
)

hvac = st.selectbox(
    "HVAC Usage",
    ["Off", "On"]
)

lighting = st.selectbox(
    "Lighting Usage",
    ["Off", "On"]
)

renewable = st.number_input(
    "Renewable Energy",
    value=10.0
)

holiday = st.selectbox(
    "Holiday",
    ["No", "Yes"]
)

hour = st.slider(
    "Hour",
    0,
    23,
    12
)

month = st.slider(
    "Month",
    1,
    12,
    6
)

day = st.selectbox(
    "Day of Week",
    [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
)


# ==========================================
# Prediction
# ==========================================

if st.button("Predict"):

    input_data = pd.DataFrame([{
        "Temperature": temperature,
        "Humidity": humidity,
        "SquareFootage": square_footage,
        "Occupancy": occupancy,
        "HVACUsage": 1 if hvac == "On" else 0,
        "LightingUsage": 1 if lighting == "On" else 0,
        "RenewableEnergy": renewable,
        "Holiday": 1 if holiday == "Yes" else 0,
        "DayOfWeek_Monday": 1 if day == "Monday" else 0,
        "DayOfWeek_Saturday": 1 if day == "Saturday" else 0,
        "DayOfWeek_Sunday": 1 if day == "Sunday" else 0,
        "DayOfWeek_Thursday": 1 if day == "Thursday" else 0,
        "DayOfWeek_Tuesday": 1 if day == "Tuesday" else 0,
        "DayOfWeek_Wednesday": 1 if day == "Wednesday" else 0,
        "Hour": hour,
        "Month": month
    }])

    prediction = model.predict(input_data)

    st.success("Prediction completed successfully!")

    st.metric(
        label="Predicted Energy Consumption",
        value=f"{prediction[0]:.2f} kWh"
    )