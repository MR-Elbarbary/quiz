import sqlite3
import random

# Path to the database file
db_path = 'project/quiz.db'  # Specify the relative path to the database file

# Connect to the database
conn = sqlite3.connect(db_path)

# Create a cursor object to interact with the database
db = conn.cursor()

# Execute the SQL query
db.execute("SELECT * FROM temp LIMIT 1")

# Fetch the result
result = db.fetchone()
print(result)

n = -1
while n not in range(1,71):
    n = int(input("Enter how many questions from 1 to 70: "))
array = []
while len(array) < n:
    temp = random.randint(1, 70)
    if temp not in array:
        array.append(temp)

score = 0
for number in array:
    # Execute the SQL query
    db.execute("SELECT * FROM quiz WHERE id = ?", (int(number),))

    # Fetch the result
    quiz = db.fetchone()
    print(quiz[1])
    print("a)",quiz[2])
    print("b)",quiz[3])
    print("c)",quiz[4])
    print("d)",quiz[5])
    ans = input()
    if ans == quiz[6]:
        score +=1
        print("correct!")
    else:
        print("wrong")
print(score)

# Close the connection
conn.close()