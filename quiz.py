import random
import datetime

ALL_QUESTIONS = {
    "PYTHON": [
        ("What keyword is used to define a function?", ["func", "def", "define", "function"], 2),
        ("What is the output of 2**3?", ["6", "8", "9", "5"], 2),
        ("How do you add a comment in Python?", ["// This", "# This", "/* This */", ""], 2),
        ("What function gets the length of a list?", ["size()", "count()", "len()", "length()"], 3),
        ("Which of these is NOT a Python data type?", ["int", "char", "str", "bool"], 2)
    ],
    "DSA": [
        ("What does 'LIFO' stand for?", ["Last In, First Out", "List In, File Out", "Large In, Fast Out", "Last In, Fast Out"], 1),
        ("A Queue follows which principle?", ["LIFO", "FIFO", "FILO", "LILO"], 2),
        ("What is the time complexity of a binary search?", ["O(n)", "O(n^2)", "O(log n)", "O(1)"], 3),
        ("Which data structure is best for an 'undo' feature?", ["Queue", "Stack", "Array", "Tree"], 2),
        ("What is a node with no children in a tree called?", ["Root Node", "Parent Node", "Sibling Node", "Leaf Node"], 4)
    ],
    "DBMS": [
        ("What does SQL stand for?", ["Strong Query Language", "Sequential Query List", "Structured Query Language", "Software Query Logic"], 3),
        ("Which SQL command is used to retrieve data?", ["GET", "RETRIEVE", "SELECT", "FETCH"], 3),
        ("Which command adds new data into a database?", ["ADD", "INSERT", "UPDATE", "CREATE"], 2),
        ("A 'Primary Key' must contain what?", ["Unique values", "Text only", "Numbers only", "A foreign key"], 1),
        ("Which command is used to change data in a table?", ["MODIFY", "CHANGE", "UPDATE", "INSERT"], 3)
    ]
}

ALL_SCORES = []

def load_questions(category):
    if category not in ALL_QUESTIONS:
        return []
    
    questions_list = ALL_QUESTIONS[category].copy()
    random.shuffle(questions_list)
    return questions_list[:5]

def save_score(enrollment_no, category, score, total):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
    score_data = f"{enrollment_no},{category},{score}/{total},{timestamp}"
    ALL_SCORES.append(score_data)
    print("Score saved temporarily.")

def run_quiz(user_enrollment_no):
    print("Welcome to the Quiz")
    print("Select a category:")
    print(" 1. PYTHON")
    print(" 2. DSA")
    print(" 3. DBMS")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        category = "PYTHON"
    elif choice == '2':
        category = "DSA"
    elif choice == '3':
        category = "DBMS"
    else:
        print("Invalid choice. Returning to menu.")
        return

    questions = load_questions(category)
    
    if not questions:
        print(f"No questions found for {category}.")
        return

    score = 0
    total = len(questions)
    print(f"Starting {category} quiz.({total} questions total)")
    
    question_number = 0
    for (question, options, correct_index) in questions:
        question_number += 1
        
        print(f"Q{question_number}: {question}")
        
        for i in range(len(options)):
            print(f"  {i+1}. {options[i]}")
        
        answer_str = input("Enter your answer (1-4): ")
        
        if answer_str.isdigit():
            answer = int(answer_str)
            if answer == correct_index:
                print("Correct.")
                score += 1
            else:
                print(f"Wrong. The correct answer was {correct_index}. {options[correct_index-1]}")
        else:
            print("Invalid input. Marking as incorrect.")

    print(f"Quiz Over")
    print(f"You scored {score} out of {total}.")
    
    save_score(user_enrollment_no, category, score, total)
    input("Press Enter to return to the main menu")

def view_all_scores():
    print("All Quiz Scores")
    if not ALL_SCORES:
        print("No scores recorded in this session yet.")
        
    for line in ALL_SCORES:
        print(f"  {line}")
    input("Press Enter to return to the admin menu")