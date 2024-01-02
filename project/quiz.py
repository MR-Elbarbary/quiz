import sqlite3
import random
import os

# Get the current working directory
current_directory = os.getcwd()

# Path to the database file within the current working directory
db_file_path = os.path.join(current_directory, 'quiz.db')

# Connect to the database
conn = sqlite3.connect(db_file_path)
# Create a cursor object to interact with the database
db = conn.cursor()

n = -1
while n not in range(1,71):
    n = int(input("Enter how many questions from 1 to 69: "))
array = []
while len(array) < n:
    temp = random.randint(1, 69)
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
    ans = input("answer: ")
    if ans == quiz[6]:
        score +=1
        print("correct!")
    else:
        print("wrong")
print(score ,"out of ", n)

# Close the connection
conn.close()