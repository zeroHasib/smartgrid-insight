import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import joblib


df = pd.read_csv("data/featured_energy_data.csv")

print(df.shape)
print(df.columns)


#in this project target  value EC:

y = df["EnergyConsumption"]

x = df.drop("EnergyConsumption", axis = 1)
print("X Shape:", x.shape)
print("y Shape:", y.shape)



x_train,x_test, y_train, y_test = train_test_split(
    x,y,test_size=0.2,random_state=42
)
print("Training Data:", x_train.shape)
print("Testing Data:", x_test.shape)


model = LinearRegression()
model.fit (x_train,y_train)
print("Trained succefully")

predictions = model.predict(x_test)
print(predictions[:10])

#mae uses

mae = mean_absolute_error(y_test,predictions)
r2 = r2_score(y_test,predictions)

print("MAE:", mae)
print("R2 Score :", r2)

plt.scatter(y_test, predictions)

plt.xlabel("Actual Energy Consumption")
plt.ylabel("Predicted Energy Consumption")
plt.title("Actual vs Predicted")

plt.scatter(y_test, predictions)

plt.xlabel("Actual Energy Consumption")
plt.ylabel("Predicted Energy Consumption")
plt.title("Actual vs Predicted")

plt.savefig("outputs/actual_vs_predicted.png")
plt.close()


feature_importance = pd.DataFrame({
    "Feature": x.columns,
    "Coefficient": model.coef_
})

print(
    feature_importance.sort_values(
        by="Coefficient",
        ascending=False
    )
)



rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(x_train, y_train)
rf_predictions = rf_model.predict(x_test)

rf_mae = mean_absolute_error(y_test, rf_predictions)
rf_r2 = r2_score(y_test, rf_predictions)

print("RF MAE:", rf_mae)
print("RF R2:", rf_r2)
print("Random forest succesfully test")



joblib.dump(model, "models/energy_model.pkl")
print("Model saved successfully!")



feature_importance = pd.DataFrame({
    "Feature": x.columns,
    "Coefficient": model.coef_
})


import os

os.makedirs("outputs", exist_ok=True)

feature_importance = feature_importance.sort_values(
    by="Coefficient",
    ascending=False
)

plt.figure(figsize=(10,6))

plt.barh(
    feature_importance["Feature"],
    feature_importance["Coefficient"]
)

plt.xlabel("Coefficient Value")
plt.ylabel("Features")
plt.title("Feature Importance")

plt.tight_layout()

plt.savefig("outputs/feature_importance.png")

plt.close()

print("Feature Importance Graph Saved!")