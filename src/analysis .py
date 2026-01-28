import pandas as pd

# Load dataset
df = pd.read_csv("data/insurance.csv")

# Preview data
print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataset shape (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nMissing values per column:")
print(df.isnull().sum())
df.columns = df.columns.str.lower().str.replace(" ", "_")

print("\nCleaned column names:")
print(df.columns)
print("\nUnique values:")
print("sex:", df["sex"].unique())
print("smoker:", df["smoker"].unique())
print("region:", df["region"].unique())
print("\nAverage insurance charge:")
print(df["charges"].mean())

print("\nMedian insurance charge:")
print(df["charges"].median())

print("\nMinimum and maximum charges:")
print(df["charges"].min(), df["charges"].max())

# Charges by smoker status
smoker_charges = df.groupby("smoker")["charges"].mean()

print("\nAverage charges by smoker status:")
print(smoker_charges)

print("\nAverage charges by sex:")
print(df.groupby("sex")["charges"].mean())

print("\nAverage charges by region:")
print(df.groupby("region")["charges"].mean())

df["age_band"] = pd.cut(
    df["age"],
    bins=[0, 18, 30, 45, 60, 100],
    labels=["0-18", "19-30", "31-45", "46-60", "60+"]
)

print("\nAverage charges by age band:")
print(df.groupby("age_band")["charges"].mean())

