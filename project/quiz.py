import sqlite3

# Path to the database file
db_path = 'project/quiz.db'  # Specify the relative path to the database file

# Connect to the database
conn = sqlite3.connect(db_path)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute the SQL query
cursor.execute("SELECT * FROM temp LIMIT 1")

# Fetch the result
result = cursor.fetchone()
print(result)

# Close the connection
conn.close()