import pyodbc

# Define connection string
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=your_server;"
    "DATABASE=your_database;"
    "UID=your_username;"
    "PWD=your_password;"
    "Trusted_Connection=yes;"
)

# Create a cursor
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE Users (
        ID INT PRIMARY KEY IDENTITY(1,1),
        Name VARCHAR(100),
        Email VARCHAR(100) UNIQUE
    )
''')
conn.commit()

cursor.execute("INSERT INTO Users (Name, Email) VALUES (?, ?)", ("John Doe", "john@example.com"))
conn.commit()

cursor.execute("SELECT * FROM Users")
for row in cursor.fetchall():
    print(row)

cursor.execute("UPDATE Users SET Name = ? WHERE ID = ?", ("Jane Doe", 1))
conn.commit()

cursor.execute("DELETE FROM Users WHERE ID = ?", (1))
conn.commit()

cursor.close()
conn.close()
