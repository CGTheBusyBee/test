

# Write a program that checks which of the passwords inside PASSWORDS meet the 3 following criteria:
# 1. Minimum characters of 7
# 2. Must contain at least one special character (defined in SPECIAL-CHARACTERS)
# 3. Must include at least one number
# Tip: You may want to loop over PASSWORDS and use multiple if conditions


MIN_CHARACTERS = 7
SPECIAL_CHARS = ['!', '?', '#', '@', '$', '*']
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

PASSWORDS = ['helloWorld', 'imcisamazing 69', 'ilovecookies!23', 'python1s@mazingLanguage']

HAS_7_CHARS = False
HAS_SPECIAL_CHAR = False
HAS_NUMBER = False

def pass_checker(password):
    has_7_chars = len(password) >= MIN_CHARACTERS
    has_special_char = any(char in SPECIAL_CHARS for char in password)
    has_number = any(char.isdigit() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)

    if not has_7_chars:
        return "Password must be at least 7 characters long."
    if not has_special_char:
        return "Password must have at least one special character (!?#@$*)."
    if not has_number:
        return "Password must have at least one number."
    if not has_uppercase:
        return "Password must have at least one uppercase letter."
    if not has_lowercase:
        return "Password must have at least one lowercase letter."
    
    if len(password) > 12 and sum(char.isdigit() for char in password) > 1 and sum(char in SPECIAL_CHARS for char in password) > 1:
        return "Very strong password!"
    
    return "Strong password!"
    

def main():
    print(f"""
Welcome to the password Checker!
A strong password must meet the following criteria:
- At least {MIN_CHARACTERS} characters long
- Include at least 1 special character {SPECIAL_CHARS}
- Include at least 1 number
- At least 1 uppercase letter
- At least 1 lowercase letter
""")
    
    retry_limit = 3
    attempts = 0
    
    while attempts < retry_limit:
        password = input("Enter your password to check strength: ")
        result = pass_checker(password)

        print(result)

        if "Strong password!" in result or "Very strong password" in result:
            break

        attempts += 1
        if attempts < retry_limit:
            print(f"You have {retry_limit - attempts} attempt(s) left. Please try again.")
        else:
            print("You've reached the maximum number of attempts.")

    print("\nChecking predefined passwords:")
    for pwd in PASSWORDS:
        print(f"Password: {pwd} -> {pass_checker(pwd)}")

if __name__ == "__main__":
    main()
# import re

# def check_password_strength(password):
#     # Criteria for a strong password
#     special_characters = re.compile('[!@#$%^&*(),.?":{}|<>]')
#     numbers = re.compile('[0-9]')
#     uppercase = re.compile('[A-Z]')
#     lowercase = re.compile('[a-z]')
    
#     # Check password length
#     if len(password) < 7:
#         return "Password must be at least 7 characters long."
    
#     # Check for special characters
#     if not special_characters.search(password):
#         return "Password must include at least one special character (!@#$%^&*(),.?\":{}|<>)."
    
#     # Check for numbers
#     if not numbers.search(password):
#         return "Password must include at least one number."
    
#     # Bonus: Check for uppercase and lowercase letters
#     if not uppercase.search(password):
#         return "Password must include at least one uppercase letter."
#     if not lowercase.search(password):
#         return "Password must include at least one lowercase letter."
    
#     # Determine if the password is very strong
#     if len(password) > 12 and len(numbers.findall(password)) > 1 and len(special_characters.findall(password)) > 1:
#         return "Very strong password!"
    
#     return "Strong password!"

# def main():
#     print("Welcome to the Password Checker Program!")
#     print("A strong password must meet the following criteria:")
#     print("- At least 7 characters long")
#     print("- At least 1 special character (!@#$%^&*(),.?\":{}|<>)")
#     print("- At least 1 number")
#     print("- At least 1 uppercase letter")
#     print("- At least 1 lowercase letter")
    
#     retry_limit = 3
#     attempts = 0
    
#     while attempts < retry_limit:
#         password = input("\nEnter a password to check its strength: ")
#         result = check_password_strength(password)
        
#         print(result)
        
#         if "Strong password!" in result or "Very strong password!" in result:
#             break
        
#         attempts += 1
#         if attempts < retry_limit:
#             print(f"You have {retry_limit - attempts} attempt(s) left. Please try again.")
#         else:
#             print("You've reached the maximum number of attempts.")

# if __name__ == "__main__":
#     main()
