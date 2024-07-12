

def dollarizer(word):
    return word.replace('s', '$')

def eurizer(word):
    return word.replace('e', '3')

def replacer(word, char1, char2):
    return word.replace(char1, char2)

def wonky_text(word):
    word = replacer(word, 's', '$')
    word = replacer(word, 'e', '3')
    word = replacer(word, 'a', '8')
    return word

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def age_in_days(age_in_years):
    age = age_in_years * 365
    return age

def simple_interest(principal, rate, years):
    interest = principal * rate * years
    return interest

def plan_finances(principal, rate, years, desired_amount):
    interest = simple_interest(principal, rate, years)
    final_amount = principal + interest

    return final_amount >= principal


print(f"Dollarizer: {dollarizer("testcase")}")
print(f"Eurizer: {eurizer("testcase")}")
print(f"Replacer: {replacer("testcase", 'e','E')}")
print(f"Wonky Text: {wonky_text("testcase")}")
print(f"Celsius to Fahrenheit: {celsius_to_fahrenheit(25)}")
print(f"Age in Days: {age_in_days(26)}")
print(f"Simple Interest: {simple_interest(2000, 0.25, 5)}")
print(f"Plan Finances: {plan_finances(2000, 0.25, 5, 3000)}")