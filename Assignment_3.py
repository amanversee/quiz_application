import random
import sqlite3

# Database setup
DB_NAME = "quiz_app.db"

def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Create Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    # Create QuizResults table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS QuizResults (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            score INTEGER NOT NULL,
            FOREIGN KEY (username) REFERENCES Users(username)
        )
    """)
    conn.commit()
    conn.close()

# Quiz questions with 3 choices each
questions = [
    {"question": "What is the capital of France?", "choices": ["1. Paris", "2. London", "3. Rome"], "answer": 1},
    {"question": "Which planet is known as the Red Planet?", "choices": ["1. Earth", "2. Mars", "3. Jupiter"], "answer": 2},
    {"question": "What is the largest mammal?", "choices": ["1. Elephant", "2. Blue Whale", "3. Giraffe"], "answer": 2},
    {"question": "Which language is used for web apps?", "choices": ["1. Python", "2. JavaScript", "3. C++"], "answer": 2},
    {"question": "What is the smallest prime number?", "choices": ["1. 1", "2. 2", "3. 3"], "answer": 2},
]

# Function to register a new user
def register():
    print("\n--- Registration ---")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("Registration successful!")
    except sqlite3.IntegrityError:
        print("Username already exists. Please try another one.")
    finally:
        conn.close()

# Function to log in a user
def login():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        print("Login successful!")
        return username
    else:
        print("Incorrect username or password. Please try again.")
        return None

# Function to conduct the quiz
def attempt_quiz():
    print("\n--- Quiz Time ---")
    selected_questions = random.sample(questions, 5)  # Pick 5 random questions
    score = 0
    for idx, q in enumerate(selected_questions, 1):
        print(f"\nQ{idx}: {q['question']}")
        for choice in q["choices"]:
            print(choice)
        try:
            answer = int(input("Enter your choice (1/2/3): "))
            if answer == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Wrong!")
        except ValueError:
            print("Invalid input. Moving to next question.")
    return score

# Function to save quiz results
def save_result(username, score):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO QuizResults (username, score) VALUES (?, ?)", (username, score))
    conn.commit()
    conn.close()

# Function to show the result and allow retry
def result(username, score):
    print(f"\nYour final score is: {score}/5")
    save_result(username, score)
    retry = input("Would you like to retry the quiz? (yes/no): ").lower()
    if retry == 'yes':
        return True
    else:
        print("Thanks for playing! Goodbye!")
        return False

# Main function for the quiz application
def quiz_app():
    print("\nWelcome to the Quiz App!")
    while True:
        choice = input("\nDo you want to Register or Login? (register/login/exit): ").lower()
        if choice == 'register':
            register()
        elif choice == 'login':
            username = login()
            if username:
                while True:
                    score = attempt_quiz()
                    if not result(username, score):
                        break
            else:
                continue
        elif choice == 'exit':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'register', 'login', or 'exit'.")

# Initialize the database and run the quiz app
setup_database()
quiz_app()
