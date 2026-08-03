#categorical columns in this project is:
"""
HVACUsage      -> On / Off
LightingUsage -> On / Off
Holiday       -> Yes / No
DayOfWeek     -> Monday ... Sunday
"""
import pandas as pd 

df = pd.read_csv("data/electricity_consumption.csv")




df["HVACUsage"] = df["HVACUsage"].map({
    "On": 1,
    "Off": 0
})


df["LightingUsage"] = df["LightingUsage"].map({
    "On": 1,
    "Off": 0
})

df["Holiday"] = df["Holiday"].map({
    "Yes": 1,
    "No": 0
})
#for this use one hot coding

df = pd.get_dummies(
    df,
    columns=["DayOfWeek"],
    drop_first=True
)

df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df["Hour"] = df["Timestamp"].dt.hour
df["Month"] = df["Timestamp"].dt.month
df = df.drop("Timestamp", axis=1)

print(df.head())
print(df.dtypes)

#bool-> int
bool_columns = df.select_dtypes(include="bool").columns
df[bool_columns] = df[bool_columns].astype(int)
print(df.dtypes)


df.to_csv(
    "data/featured_energy_data.csv",
    index=False
)

print("Feature Engineering Completed!")