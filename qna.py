def ask_question(question, choices, correct_answer):
    print(question)
    for i, choice in enumerate(choices, start=1):
        print(f"{chr(64 + i)}. {choice}")
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    return user_answer == correct_answer


questions = [
    {
        "question": "What is the most popular programming language in 2023?",
        "choices": ["Python", "Java", "C++", "JavaScript"],
        "correct_answer": "A"
    },
    {
        "question": "Which data structure uses LIFO (Last In, First Out) order?",
        "choices": ["Queue", "Stack", "Heap", "Tree"],
        "correct_answer": "B"
    },
    {
        "question": "What is the time complexity of the quicksort algorithm in the average case?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
        "correct_answer": "B"
    },
    {
        "question": "What is the binary representation of the decimal number 10?",
        "choices": ["1010", "1001", "1100", "1111"],
        "correct_answer": "A"
    },
    {
        "question": "Which sorting algorithm has the best average-case time complexity?",
        "choices": ["Bubble Sort", "Merge Sort", "Quick Sort", "Selection Sort"],
        "correct_answer": "B"
    }
]

correct_answers = 0

print("Welcome to the Computer Science Quiz!\n")

for question in questions:
    if ask_question(question["question"], question["choices"], question["correct_answer"]):
        print("Correct!\n")
        correct_answers += 1
    else:
        print(f"Incorrect. The correct answer is: {question['correct_answer']}\n")

grade = (correct_answers / len(questions)) * 100
print(f"You scored {correct_answers} out of {len(questions)} ({grade:.2f}%)")
