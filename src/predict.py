import joblib
import pandas as pd
# Load trained model
model = joblib.load("models/energy_model.pkl")

print("Model Loaded Successfully!")




# Load Trained Model
model = joblib.load("models/energy_model.pkl")

print("\n===== SmartGrid Insight =====\n")

# Numerical Inputs
temperature = float(input("Temperature : "))
humidity = float(input("Humidity (%): "))
square_footage = float(input("Square Footage: "))
occupancy = int(input("Occupancy: "))

# HVAC
hvac_input = input("HVAC Usage (On/Off): ").strip().lower()
hvac = 1 if hvac_input == "on" else 0

# Lighting
lighting_input = input("Lighting Usage (On/Off): ").strip().lower()
lighting = 1 if lighting_input == "on" else 0

# Renewable Energy
renewable = float(input("Renewable Energy: "))

# Holiday
holiday_input = input("Holiday (Yes/No): ").strip().lower()
holiday = 1 if holiday_input == "yes" else 0

# Time Features
hour = int(input("Hour (0-23): "))
month = int(input("Month (1-12): "))

# Day of Week
day = input(
    "Day of Week (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): "
).strip().capitalize()

# One-Hot Encoding
day_monday = 1 if day == "Monday" else 0
day_saturday = 1 if day == "Saturday" else 0
day_sunday = 1 if day == "Sunday" else 0
day_thursday = 1 if day == "Thursday" else 0
day_tuesday = 1 if day == "Tuesday" else 0
day_wednesday = 1 if day == "Wednesday" else 0

# Create DataFrame
input_data = pd.DataFrame([{
    "Temperature": temperature,
    "Humidity": humidity,
    "SquareFootage": square_footage,
    "Occupancy": occupancy,
    "HVACUsage": hvac,
    "LightingUsage": lighting,
    "RenewableEnergy": renewable,
    "Holiday": holiday,
    "DayOfWeek_Monday": day_monday,
    "DayOfWeek_Saturday": day_saturday,
    "DayOfWeek_Sunday": day_sunday,
    "DayOfWeek_Thursday": day_thursday,
    "DayOfWeek_Tuesday": day_tuesday,
    "DayOfWeek_Wednesday": day_wednesday,
    "Hour": hour,
    "Month": month
}])

# Prediction
prediction = model.predict(input_data)

print("\n===== Prediction Result =====")
print(f"Predicted Energy Consumption: {prediction[0]:.2f} kWh")