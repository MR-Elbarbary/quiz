import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute the SQL query
cursor.execute("SELECT * FROM temp WHERE id = ?", (1,))

# Fetch the result
result = cursor.fetchone()
print(result)

# Close the connection
conn.close()
