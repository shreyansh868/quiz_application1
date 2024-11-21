def display_welcome():
    print("Welcome to the Quiz Application!")
    print("Answer the following questions by selecting the option number (e.g., 1, 2, 3, or 4).")
    print("-" * 50)

def get_questions():
    return [
        {
            "question": "What arithmetic operators cannot be used with strings in Python?",
            "options": ["1. *", "2. –", "3. +", "4. All of the mentioned"],
            "answer": 2
        },
        {
            "question": "Which programming language is known as the language of the web?",
            "options": ["1. Python", "2. JavaScript", "3. C++", "4. Java"],
            "answer": 2
        },
        {
            "question": "Which of the following is not a core data type in Python programming?",
            "options": ["1. Tuples", "2. Lists", "3. Class", "4. Dictionary"],
            "answer": 3
        },
        {
            "question": "Which keyword is used for function in Python language?",
            "options": ["1. Function", "2. def", "3. Fun", "4. Define"],
            "answer": 2
        },
        {
            "question": "What does pip stand for python?",
            "options": ["1. Pip Installs Python", "2. Pip Installs Packages", "3. Preferred Installer Program", "4. All of the mentioned"],
            "answer": 3
        },
        {
            "question": "Which of the following is a Python tuple?",
            "options": ["1. {1, 2, 3}", "2. { }", "3. [1, 2, 3]", "4. (1, 2, 3)"],
            "answer": 4
        }
    ]

def ask_question(question):
    print("\n" + question["question"])
    for option in question["options"]:
        print(option)
    while True:
        try:
            user_answer = int(input("Enter your answer (1-4): "))
            if 1 <= user_answer <= 4:
                return user_answer
            else:
                print("Invalid choice. Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_score(questions, user_answers):
    score = 0
    for i, question in enumerate(questions):
        if user_answers[i] == question["answer"]:
            score += 1
    return score

def display_results(score, total_questions):
    print("\nQuiz Completed!")
    print(f"Your Score: {score}/{total_questions}")
    if score == total_questions:
        print("Excellent! You got all answers correct.")
    elif score > total_questions // 2:
        print("Good job! You did well.")
    else:
        print("Keep practicing. Better luck next time!")

def main():
    display_welcome()
    questions = get_questions()
    user_answers = []
    
    for question in questions:
        user_answer = ask_question(question)
        user_answers.append(user_answer)
    
    score = calculate_score(questions, user_answers)
    display_results(score, len(questions))

if __name__ == "__main__":
    main()
