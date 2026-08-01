import pandas as pd
df = pd.read_csv("transactions.csv")
print("Original Data:")
print(df)
df.replace(r"^\s*$", pd.NA, regex=True, inplace=True)

duplicate_records = df[
    df.duplicated(
        subset="transaction_id",
        keep=False
    )
]
print("\nDuplicate Transactions:")
print(duplicate_records)
df.drop_duplicates(
    subset="transaction_id",
    keep="first",
    inplace=True
)
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.lower()
)
type_mapping = {
    "deposit": "Deposit",
    "withdraw": "Withdrawal",
    "withdrawal": "Withdrawal",
    "transfer": "Transfer"
}
df["transaction_type"] = (
    df["transaction_type"]
    .map(type_mapping)
)
invalid_transactions = df[
    df["account_number"].isnull() |
    df["transaction_type"].isnull() |
    (df["amount"] <= 0)
]
print("\nInvalid Transactions:")
print(invalid_transactions)

valid_transactions = df.drop(
    invalid_transactions.index
)
valid_transactions.to_csv(
    "cleaned_transactions.csv",
    index=False
)
invalid_transactions.to_csv(
    "invalid_transactions.csv",
    index=False
)
print("\nCleaned Transactions:")
print(valid_transactions)
print(
    "\nProcessed data saved as "
    "cleaned_transactions.csv"
)