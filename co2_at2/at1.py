import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

# Create Student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    Student_ID INTEGER PRIMARY KEY,
    Student_Name TEXT,
    Department TEXT
)
""")

# Create Course table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Course (
    Course_ID INTEGER PRIMARY KEY,
    Course_Name TEXT,
    Credits INTEGER
)
""")

# Create Enrollment table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Enrollment (
    Enrollment_ID INTEGER PRIMARY KEY,
    Student_ID INTEGER,
    Course_ID INTEGER,
    Semester TEXT,
    FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID),
    FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID)
)
""")

# Clear old data
cursor.execute("DELETE FROM Enrollment")
cursor.execute("DELETE FROM Student")
cursor.execute("DELETE FROM Course")

# Insert Student data
students = [
    (1, "Alice", "CSE"),
    (2, "Bob", "ECE"),
    (3, "Charlie", "IT"),
    (4, "David", "CSE")
]

cursor.executemany("INSERT INTO Student VALUES (?, ?, ?)", students)

# Insert Course data
courses = [
    (101, "Database Systems", 4),
    (102, "Python Programming", 3),
    (103, "Machine Learning", 5),
    (104, "Operating Systems", 4)
]

cursor.executemany("INSERT INTO Course VALUES (?, ?, ?)", courses)

# Insert Enrollment data
enrollments = [
    (1, 1, 101, "Semester 1"),
    (2, 2, 102, "Semester 1"),
    (3, 3, 103, "Semester 2"),
    (4, 4, 104, "Semester 1"),
    (5, 1, 103, "Semester 2")
]

cursor.executemany("INSERT INTO Enrollment VALUES (?, ?, ?, ?)", enrollments)

conn.commit()

# Query
cursor.execute("""
SELECT
    s.Student_Name,
    c.Course_Name,
    e.Semester
FROM Student s
JOIN Enrollment e
    ON s.Student_ID = e.Student_ID
JOIN Course c
    ON e.Course_ID = c.Course_ID
WHERE c.Credits > 3
""")

# Display Result
print("Students Enrolled in Courses Carrying More Than 3 Credits")
print("-" * 60)

rows = cursor.fetchall()

for row in rows:
    print("Student Name :", row[0])
    print("Course Name  :", row[1])
    print("Semester     :", row[2])
    print("-" * 60)

conn.close()