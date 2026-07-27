import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",
    database="db1"
)

cursor = conn.cursor()

# Create Account table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Account(
    Account_No INT PRIMARY KEY,
    Customer_Name VARCHAR(50) NOT NULL,
    Account_Type VARCHAR(20) NOT NULL,
    Balance DECIMAL(10,2) NOT NULL CHECK (Balance >= 0)
)
""")

# Insert customer account records
accounts = [
    (1001, "John", "Savings", 25000.00),
    (1002, "Alice", "Current", 18000.00),
    (1003, "David", "Savings", 32000.00)
]

cursor.executemany("""
INSERT INTO Account(Account_No, Customer_Name, Account_Type, Balance)
VALUES (%s, %s, %s, %s)
""", accounts)

# Update account balance after a transaction
cursor.execute("""
UPDATE Account
SET Balance = Balance + 5000
WHERE Account_No = 1001
""")

# Retrieve account information
cursor.execute("SELECT * FROM Account")

print("Account Details")
print("-" * 60)

for row in cursor.fetchall():
    print(row)

# Commit changes
conn.commit()

# Close connection
cursor.close()
conn.close()