import json
import pandas as pd

with open("books.json", "r") as file:
    data = json.load(file)
df = pd.DataFrame(data)
print("Original Data:")
print(df)
required_fields = [
    "book_id",
    "title",
    "author",
    "publisher",
    "year"
]
missing_columns = [
    col for col in required_fields
    if col not in df.columns
]
if missing_columns:
    print("\nMissing Required Fields:")
    print(missing_columns)
df.replace(r"^\s*$", pd.NA, regex=True, inplace=True)
invalid_records = df[df.isnull().any(axis=1)]
print("\nInvalid Records:")
print(invalid_records)
df.dropna(subset=required_fields, inplace=True)
df["book_id"] = df["book_id"].str.strip().str.upper()
df["title"] = df["title"].str.strip().str.title()
df["author"] = df["author"].str.strip().str.title()
df["publisher"] = df["publisher"].str.strip().str.title()
df["year"] = pd.to_numeric(
    df["year"],
    errors="coerce"
)
df = df[
    (df["year"] >= 1000) &
    (df["year"] <= 2026)
]
df.to_csv("cleaned_books.csv", index=False)
print("\nCleaned Dataset:")
print(df)
print("\nCleaned data saved as cleaned_books.csv")