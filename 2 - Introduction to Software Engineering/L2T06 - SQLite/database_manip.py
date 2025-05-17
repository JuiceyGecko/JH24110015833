"""Using SQLite3 to create a database and manipulate data"""

import sqlite3

# Connect to database provided
db = sqlite3.connect('python_programming.db')
cursor = db.cursor()

# Debug: Start of script
cursor.execute("DROP TABLE IF EXISTS python_programming")

# Create table for students
cursor.execute('''
    CREATE TABLE python_programming (
        id INTEGER PRIMARY KEY,
        name TEXT,
        grade INTEGER
    )
''')
print("Table created.")

# Insert data into created table
students = [
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
]
cursor.executemany('INSERT INTO python_programming VALUES(?,?,?)', students)
print(f"Inserted {len(students)} records.")

# Select records with grade 60-80
cursor.execute('SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80')
print("Grades 60-80 (BEFORE updates):", cursor.fetchall())

# Update Carl Davis's grade to 65
cursor.execute('UPDATE python_programming SET grade = 65 WHERE name = "Carl Davis"')
print("Updated Carl Davis's grade.")

# Delete Dennis Fredrickson from the table
cursor.execute('DELETE FROM python_programming WHERE name = "Dennis Fredrickson"')
print("Deleted Dennis Fredrickson.")

# Update grades of the given ID's; id > 55
cursor.execute('UPDATE python_programming SET grade = 80 WHERE id > 55')
print("Updated grades for id > 55.")

# Printing data to see if the updates worked
cursor.execute('SELECT * FROM python_programming')
print("FINAL DATA:", cursor.fetchall())

db.commit()
db.close()
