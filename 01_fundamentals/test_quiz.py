import random

# Sample dictionary of categories, questions, multiple choice answers, and the correct answer
quiz = {
    "Science": {
        "What is the powerhouse of the cell?": {
            "choices": ["A. Nucleus", "B. Mitochondria", "C. Ribosome", "D. Endoplasmic Reticulum"],
            "answer": "B"
        },
        "Which planet is known as the Red Planet?": {
            "choices": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
            "answer": "B"
        }
    },
    "History": {
        "Who was the first President of the United States?": {
            "choices": ["A. George Washington", "B. Thomas Jefferson", "C. Abraham Lincoln", "D. John Adams"],
            "answer": "A"
        },
        "In which year did the Titanic sink?": {
            "choices": ["A. 1905", "B. 1912", "C. 1923", "D. 1918"],
            "answer": "B"
        }
    }
}

def add_new_question(category):
    question = input("Enter the new question: ")
    choices = []
    for i in range(4):
        choice = input(f"Enter choice {chr(65 + i)}: ")
        choices.append(f"{chr(65 + i)}. {choice}")
    correct_answer = input("Enter the correct answer (A, B, C, D): ").strip().upper()
    
    if category in quiz:
        quiz[category][question] = {"choices": choices, "answer": correct_answer}
    else:
        quiz[category] = {question: {"choices": choices, "answer": correct_answer}}

    print(f"New question added to the {category} category.")

def conduct_quiz(quiz, category):
    score = 0
    correct_questions = []
    incorrect_questions = []

    questions = list(quiz[category].items())
    random.shuffle(questions)

    for question, data in questions:
        print(question)
        for choice in data["choices"]:
            print(choice)
        
        valid_answer = False
        while not valid_answer:
            answer = input("Please select an option (A, B, C, D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                valid_answer = True
                if answer == data["answer"]:
                    print(f"You selected: {answer} - Correct!")
                    score += 1
                    correct_questions.append(question)
                else:
                    print(f"You selected: {answer} - Incorrect. The correct answer is {data['answer']}.")
                    incorrect_questions.append((question, data["answer"]))
            else:
                print("Invalid option. Please choose A, B, C, or D.")
        print()  # Blank line for readability between questions

    # Print the final score and summary of answers
    print(f"\nQuiz Completed! Your final score is: {score}/{len(questions)}")
    print("\nQuestions you answered correctly:")
    for q in correct_questions:
        print(f"- {q}")
    print("\nQuestions you answered incorrectly:")
    for q, correct_answer in incorrect_questions:
        print(f"- {q} (Correct answer: {correct_answer})")

def main():
    chosen_categories = set()
    
    while True:
        remaining_categories = set(quiz.keys()) - chosen_categories
        if not remaining_categories:
            print("All categories have been chosen. Exiting the quiz.")
            break
        
        print("Select a category:")
        for i, category in enumerate(remaining_categories, start=1):
            print(f"{i}. {category}")
        print(f"{len(remaining_categories) + 1}. Add a new question")

        choice = input("Enter the number of your choice: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(remaining_categories):
            category = list(remaining_categories)[int(choice) - 1]
            conduct_quiz(quiz, category)
            chosen_categories.add(category)
        elif choice == str(len(remaining_categories) + 1):
            new_category = input("Enter the category for the new question: ").strip()
            add_new_question(new_category)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
