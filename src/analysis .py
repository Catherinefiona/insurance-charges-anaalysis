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


