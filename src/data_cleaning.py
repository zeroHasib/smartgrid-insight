import pandas as pd 
df = pd.read_csv ("data/electricity_consumption.csv")


print("Dataset Shape:")
print(df.shape)

print ("Dataset Column:")
print (df.columns)

print (df.head())

print(df.dtypes)

print("\nmissing values")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated())

print ("\nDataset Summary:")
print(df.describe())




