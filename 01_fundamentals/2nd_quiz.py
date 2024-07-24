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
        'answer': 'A'
    },
    '2. What is the shortened version of "boolean" in Python?': {
        'choices': ['A. bool', 'B. tool', 'C. fool', 'D. cool'],
        'answer': 'A'
    },
    '3. What is 23 + 71?': {
        'choices': ['A. 94', 'B. 2371', 'C. 90', 'D. 48'],
        'answer': 'A'
    },
    '4. When was Python created?': {
        'choices': ['A. 1991', 'B. 1990', 'C. 1900', 'D. 1978'],
        'answer' : 'A'
    },
    '5. To assign a variable, do we use = or ==?': {
        'choices': ['A. =', 'B. ==', 'C. +=', 'D. -='],
        'answer': 'A'
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
            answer = input('Please select an option (A, B, C, D): ').strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                valid_answer = True
                if answer == sub_dict['answer']:
                    print(f"Correct! Keep up the great work there, guy ;). Or gal lol I don't discriminate (;")
                    score += 1
                    correct_questions.append(question)
                else:
                    print(f"WROOONNNGG! You stupid or something? LMFAO the correct answer is {sub_dict['answer']}. Good luck next time stupid bitch hoe.")
                    incorrect_questions.append((question, sub_dict['answer']))
            else: 
                print('What a dumbfuck, how much clearer could we have been? ROFL')
        print()

    # Print the score with a message at the end
    print(f"\nCongratulations you sexy devil you! You have completed the ultra hard quiz with an unbelievable score of {score}/{len(quiz)}!")
    if score <= 3:
        print("\nMWAHAHAHA WHAT A DUMBFUCK! YOU AIN'T NO SEXY DEVIL WITH A SHITTY SCORE LIKE THAT. What a loser lmfao. Bye bitch. Good luck ever getting laid pussy.")
    else:
        print("\nNot too shabby there tiger. Keep it up and maybe we'll invite you over again for another quiz ;).")

    print(f"\nQuestions you answered correctly: ")
    for q in correct_questions:
        print (f'- {q}')

    print("Questions you answered incorrectly: ")
    for q, correct_answer in incorrect_questions:
        print(f'- {q} (Correct answer: {correct_answer})')


conduct_quiz(quiz)
 # for q in incorrect_questions, sub_dict['answer']:
    #     print(f'- {incorrect_questions, sub_dict['answer']}')