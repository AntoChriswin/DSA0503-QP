import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Create Customer table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customer (
    Customer_ID INTEGER PRIMARY KEY,
    Customer_Name TEXT,
    City TEXT
)
""")

# Create Account table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Account (
    Account_No INTEGER PRIMARY KEY,
    Customer_ID INTEGER,
    Account_Type TEXT,
    Balance REAL,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID)
)
""")

# Create Transactions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Transactions (
    Transaction_ID INTEGER PRIMARY KEY,
    Account_No INTEGER,
    Transaction_Date TEXT,
    Amount REAL,
    FOREIGN KEY (Account_No) REFERENCES Account(Account_No)
)
""")

# Clear old data
cursor.execute("DELETE FROM Transactions")
cursor.execute("DELETE FROM Account")
cursor.execute("DELETE FROM Customer")

# Insert Customer data
customers = [
    (1, "Arun", "Chennai"),
    (2, "Priya", "Coimbatore"),
    (3, "Rahul", "Madurai"),
    (4, "Sneha", "Trichy")
]

cursor.executemany("INSERT INTO Customer VALUES (?, ?, ?)", customers)

# Insert Account data
accounts = [
    (1001, 1, "Savings", 150000),
    (1002, 2, "Current", 85000),
    (1003, 3, "Savings", 250000),
    (1004, 4, "Current", 95000)
]

cursor.executemany("INSERT INTO Account VALUES (?, ?, ?, ?)", accounts)

# Insert Transaction data
transactions = [
    (1, 1001, "2026-08-01", 5000),
    (2, 1002, "2026-08-02", 10000),
    (3, 1003, "2026-08-03", 25000),
    (4, 1004, "2026-08-04", 15000)
]

cursor.executemany("INSERT INTO Transactions VALUES (?, ?, ?, ?)", transactions)

conn.commit()

# Query
cursor.execute("""
SELECT
    c.Customer_Name,
    a.Account_No,
    a.Balance
FROM Customer c
JOIN Account a
ON c.Customer_ID = a.Customer_ID
WHERE a.Balance > 100000;
""")

# Display Result
print("Customers with Account Balance Greater Than ₹1,00,000")
print("-" * 60)

rows = cursor.fetchall()

for row in rows:
    print("Customer Name :", row[0])
    print("Account No    :", row[1])
    print("Balance       : ₹", row[2])
    print("-" * 60)

conn.close()