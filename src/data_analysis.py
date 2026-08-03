import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("data/electricity_consumption.csv")

print("Average Energy Consumption:")
print(df["EnergyConsumption"].mean())

print("\nMaximum Energy Consumption:")
print(df["EnergyConsumption"].max())

print("\nMinimum Energy Consumption:")
print(df["EnergyConsumption"].min())

print("\nEnergy consumption by day:")
daily_usages =(df.groupby("DayOfWeek")["EnergyConsumption"].mean()) 
print(daily_usages)

print("\n Holiday Analysis")
Holiday_usages = (df.groupby("Holiday")["EnergyConsumption"].mean())
print(Holiday_usages)


Holiday_usages.plot(kind  = "bar", color = "red")

plt.title("average energy consumption by day")
plt.xlabel ("Holiday")
plt.ylabel("Energy Consumption")
plt.show()


plt.figure(figsize =(8,5))

plt.scatter(
    df["Temperature"],
    df["EnergyConsumption"]
)

plt.title("Temperature vs Energy Consumption")
plt.xlabel ("Temperature")
plt.ylabel("Energy Consumption")
plt.show()


plt.figure(figsize=(8,5))

plt.scatter(
    df["Occupancy"],
    df["EnergyConsumption"]
)

plt.title("Occupancy vs Energy Consumption")
plt.xlabel("Occupancy")
plt.ylabel("Energy Consumption")

plt.show()

print(
    df.corr(numeric_only=True)
)

print(df.dtypes)
# ml undertsand only numeric values 
print("HVACUsage:")
print(df["HVACUsage"].unique())

print("\nLightingUsage:")
print(df["LightingUsage"].unique())

print("\nHoliday:")
print(df["Holiday"].unique())

print("\nDayOfWeek:")
print(df["DayOfWeek"].unique())
