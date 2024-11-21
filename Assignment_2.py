

#Name - Aman mourya
#Enrollment no. - 0176AL2210181
#College - LNCTE
#Branch - CSE-AIML



import random
import os

# File paths for user data and quiz results
USER_FILE = "users_db.txt"
RESULTS_FILE = "quiz_results.txt"

# Function to load user data from file
def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as f:
        users = {}
        for line in f:
            username, password = line.strip().split(",")
            users[username] = password
        return users

# Function to save user data to file
def save_user(username, password):
    with open(USER_FILE, "a") as f:
        f.write(f"{username},{password}\n")

# Function to save quiz results
def save_result(username, score):
    with open(RESULTS_FILE, "a") as f:
        f.write(f"{username},{score}\n")

# Quiz questions with 3 choices each
questions = [
    {"question": "What is the capital of France?", "choices": ["1. Paris", "2. London", "3. Rome"], "answer": 1},
    {"question": "Which planet is known as the Red Planet?", "choices": ["1. Earth", "2. Mars", "3. Jupiter"], "answer": 2},
    {"question": "What is the largest mammal?", "choices": ["1. Elephant", "2. Blue Whale", "3. Giraffe"], "answer": 2},
    {"question": "Which language is used for web apps?", "choices": ["1. Python", "2. JavaScript", "3. C++"], "answer": 2},
    {"question": "What is the smallest prime number?", "choices": ["1. 1", "2. 2", "3. 3"], "answer": 2},
    {"question": "Which ocean is the largest?", "choices": ["1. Pacific", "2. Atlantic", "3. Indian"], "answer": 1},
    {"question": "What is the square root of 64?", "choices": ["1. 6", "2. 7", "3. 8"], "answer": 3},
    {"question": "What is the chemical symbol for water?", "choices": ["1. H2O", "2. CO2", "3. NaCl"], "answer": 1},
    {"question": "Which country gifted the Statue of Liberty to the USA?", "choices": ["1. France", "2. Spain", "3. Italy"], "answer": 1},
    {"question": "Who wrote 'Hamlet'?", "choices": ["1. Charles Dickens", "2. William Shakespeare", "3. Mark Twain"], "answer": 2},
]

# Function to register a new user
def register(users_db):
    print("\n--- Registration ---")
    username = input("Enter a username: ")
    if username in users_db:
        print("Username already exists. Please try another one.")
        return
    password = input("Enter a password: ")
    users_db[username] = password
    save_user(username, password)
    print("Registration successful!")

# Function to log in a user
def login(users_db):
    print("\n--- Login ---")
    username = input("Enter your username: ")
    if username not in users_db:
        print("Username not found. Please register first.")
        return None
    password = input("Enter your password: ")
    if users_db[username] == password:
        print("Login successful!")
        return username
    else:
        print("Incorrect password. Please try again.")
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
        answer = int(input("Enter your choice (1/2/3): "))
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    return score

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
    users_db = load_users()  # Load users from file
    print("\nWelcome to the Quiz App!")
    while True:
        choice = input("\nDo you want to Register or Login? (register/login/exit): ").lower()
        if choice == 'register':
            register(users_db)
        elif choice == 'login':
            username = login(users_db)
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

# Run the quiz app
quiz_app()
