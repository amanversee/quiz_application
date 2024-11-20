
#Name - Aman mourya
#Enrollment no. - 0176AL2210181
#College - LNCTE
#Branch - CSE-AIML

import random

# User database for storing user information (username and password)
users_db = {}

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
    {"question": "What is the capital of Japan?", "choices": ["1. Tokyo", "2. Beijing", "3. Seoul"], "answer": 1},
    {"question": "How many continents are there?", "choices": ["1. 5", "2. 6", "3. 7"], "answer": 3},
    {"question": "Which element is known as the King of Chemicals?", "choices": ["1. Sulfuric Acid", "2. Nitric Acid", "3. Ammonia"], "answer": 1},
    {"question": "How many bones are in the adult human body?", "choices": ["1. 206", "2. 208", "3. 210"], "answer": 1},
    {"question": "Which animal is known as the 'Ship of the Desert'?", "choices": ["1. Camel", "2. Horse", "3. Elephant"], "answer": 1},
    {"question": "Which gas do plants absorb during photosynthesis?", "choices": ["1. Oxygen", "2. Carbon Dioxide", "3. Nitrogen"], "answer": 2},
    {"question": "How many teeth does a normal adult human have?", "choices": ["1. 30", "2. 32", "3. 34"], "answer": 2},
    {"question": "Which country has the largest population?", "choices": ["1. India", "2. China", "3. USA"], "answer": 2},
    {"question": "What is the chemical formula for table salt?", "choices": ["1. NaCl", "2. KCl", "3. MgCl"], "answer": 1},
    {"question": "What is the tallest mountain in the world?", "choices": ["1. K2", "2. Mount Everest", "3. Kangchenjunga"], "answer": 2},
]

# Function to register a new user
def register():
    print("\n--- Registration ---")
    username = input("Enter a username: ")
    if username in users_db:
        print("Username already exists. Please try another one.")
        return
    password = input("Enter a password: ")
    users_db[username] = password
    print("Registration successful!")

# Function to log in a user
def login():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    if username not in users_db:
        print("Username not found. Please register first.")
        return False
    password = input("Enter your password: ")
    if users_db[username] == password:
        print("Login successful!")
        return True
    else:
        print("Incorrect password. Please try again.")
        return False

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
def result(score):
    print(f"\nYour final score is: {score}/5")
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
            if login():
                while True:
                    score = attempt_quiz()
                    if not result(score):
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
