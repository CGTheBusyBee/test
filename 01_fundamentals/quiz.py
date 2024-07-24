# questions = ['Who founded python?', 'What is the shortened version of "boolean" in Python?', 'what is 23+71?',
#              'when was Python created?', 'To assign a variable, do we use = or ==?']

# answers = ['Guido van Rossum', 'bool', '94', '1991', '=']
# Write a program that loops through the questions and adds 1 to the
# score if the player answers correctly and 0 if they answer incorrectly
# Print the score with a message of your coice at the end. 
# You may also print a different message based on how well the user did.
quiz = {
    '1. Who founded python?': {
        'choices': ['A. Guido van Rossum', 'B. Martin Luther King', 'C. Batman', 'D. Clark Kent'],
        'answer': "A"
    }, 
    '2. What is the shortened version of "boolean" in Python?': {
        'choices': ['A. bool', 'B. pool', 'C. duel', 'D. fool'],
        'answer': "A"
    }, 
    '3. What is 23+71?': {
        'choices': ['A. 94', 'B. 104', 'C. 92', 'D. 2371'],
        'answer': "A"
    },
    '4. When was Python created?': {
        'choices': ['A. 1991', 'B. 1990','C. 2000','D. 2001'],
        'answer': "A"
    }, 
    '5. To assign a variable, do we use = or ==?': {
        'choices': ['A. =', 'B. =='],
        'answer': "A"
    }
}


def conduct_quiz(quiz):
    score = 0
    correct_questions = []
    incorrect_questions = []

    for question, sub_dict in quiz.items():
        print(question)
        for choice in sub_dict['choices']:
            print(choice)
        
        valid_answer = False
        while not valid_answer:
            answer = input("Please select an option (A, B, C, D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                valid_answer = True 
                if answer == sub_dict['answer']:
                    print(f'You selected: {answer} - Correct!')
                    score += 1
                    correct_questions.append(question)
                else:
                    print(f'WROOOONNNGGGG BITCH! The correct answer is {sub_dict['answer']}.')
                    incorrect_questions.append((question, sub_dict['answer']))
            else:
                print("Invalid option. Please choose A, B, C, or D.")
        print() # Blank line for readability between questions

    # Print the final score and summary of answers
    print(f'\nQuiz Completed! your final score is: {score}/{len(quiz)}')
    print('\nQuestions you answered correctly:')
    for q in correct_questions:
        print(f'- {q}')
    print('\nQuestions you answered incorrectly:')
    for q, correct_answer in incorrect_questions:
        print(f'- {q} (Correct answer: {correct_answer})')



conduct_quiz(quiz)