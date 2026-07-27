import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create Department table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Department(
    Department_ID INTEGER PRIMARY KEY,
    Department_Name TEXT NOT NULL
)
""")

# Create Employee table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee(
    Employee_ID INTEGER PRIMARY KEY,
    Employee_Name TEXT NOT NULL,
    Salary REAL,
    Department_ID INTEGER,
    FOREIGN KEY (Department_ID) REFERENCES Department(Department_ID)
)
""")

# Insert sample data into Department table
departments = [
    (1, "HR"),
    (2, "Finance"),
    (3, "IT")
]

cursor.executemany(
    "INSERT INTO Department (Department_ID, Department_Name) VALUES (?, ?)",
    departments
)

# Insert sample data into Employee table
employees = [
    (101, "John", 50000, 1),
    (102, "Alice", 60000, 2),
    (103, "David", 70000, 3),
    (104, "Emma", 65000, 3)
]

cursor.executemany(
    "INSERT INTO Employee (Employee_ID, Employee_Name, Salary, Department_ID) VALUES (?, ?, ?, ?)",
    employees
)

# Execute INNER JOIN query
cursor.execute("""
SELECT Employee.Employee_Name,
       Department.Department_Name
FROM Employee
INNER JOIN Department
ON Employee.Department_ID = Department.Department_ID
""")

# Display the results
print("Employee Name\tDepartment")
print("-" * 30)

for row in cursor.fetchall():
    print(f"{row[0]}\t\t{row[1]}")

# Commit and close the connection
conn.commit()
conn.close()