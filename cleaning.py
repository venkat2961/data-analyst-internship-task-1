import pandas as pd

# 1. Load the original dataset
df = pd.read_csv("Sales_Dataset.csv")

print("Original dataset:")
print(df.head())

print("\nDataset shape:")
print(df.shape)


# 2. Remove unnecessary column
df = df.drop(columns=["Unnamed: 0"], errors="ignore")


# 3. Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nCleaned column names:")
print(df.columns)


# 4. Standardize text columns
df["gender"] = df["gender"].astype(str).str.strip().str.title()
df["product_category"] = (
    df["product_category"]
    .astype(str)
    .str.strip()
    .str.title()
)


# 5. Convert date column
df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)


# 6. Check missing values
print("\nMissing values:")
print(df.isnull().sum())


# 7. Check duplicate records
print("\nDuplicate records:")
print(df.duplicated().sum())


# 8. Remove duplicates
df = df.drop_duplicates()


# 9. Convert numeric columns
numeric_columns = [
    "age",
    "quantity",
    "price_per_unit",
    "total_amount"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# 10. Validate Total Amount
df["calculated_total"] = (
    df["quantity"] * df["price_per_unit"]
)

mismatches = (
    df["calculated_total"] != df["total_amount"]
).sum()

print("\nTotal amount mismatches:")
print(mismatches)


# 11. Remove temporary column
df = df.drop(columns=["calculated_total"])


# 12. Format date
df["date"] = df["date"].dt.strftime("%d-%m-%Y")


# 13. Save cleaned dataset
df.to_csv(
    "Cleaned_Sales_Dataset.csv",
    index=False
)

print("\nData cleaning completed successfully!")

print("\nFinal dataset shape:")
print(df.shape)