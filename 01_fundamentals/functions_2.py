

def dollarizer(word):
    return word.replace('s', '$')

def eurizer(word):
    return word.replace('e', '3')

def replacer(word, char1, char2):
    return word.replace(char1, char2)

def wonky_text(word):
    word = replacer(word, 's', '$')
    word = replacer(word, 'e', '3')
    word = replacer(word, '1', '#')
    return word

# create a function named celsius_to_fahrenheit that takes
# a temperature in Celsius and returns its equivalent in Fahrenheit.
# Use the formula: F=C*9/5 + 32

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# create a function nambed age_in_days that takes an age in years
# (assume whole years only) and returns the age in days (ignore leap years)
# Assume each year has 365 days

def age_in_days(age_years):
    days_in_year = 365
    age_days = age_years * days_in_year
    return age_days

# Create a function named simple_interest that calculates simple interest. 
# It should take three arguments: principal amount, rate of interest, and time in years.
#  Use the formula: ( SI = P * R * T ). Return the calculated simple interest.

def simple_interest(principal, rate, time):
    interest = (principal * rate * time)
    return interest

# Write a function named plan_finances that takes a principal amount,
# rate of interest, time in years, and a desired final amount after simple interest.
# The function should return whether the final amount after simple interest is achieved
# from the principal within the given time and rate.

def plan_finances(principal, rate, time, desired_amount):
    # Calculate the simple interest
    interest = simple_interest(principal, rate, time)
    # Calculate the final amount
    final_amount = principal + interest
    # Check if the final amount meets or exceeds the desired amount
    return final_amount >= desired_amount


print(f"Dollarizer: {dollarizer("testcase")}")
print(f"Eurizer: {eurizer("testcase")}")
print(f"Replacer: {replacer("testcase", "t", "#")}")
print(f"Wonky Text: {wonky_text("tescase")}")
print(f"Celsius to Fahrenheit: {celsius_to_fahrenheit(25)}")
print(f"Age in Days: {age_in_days(26)}")
print(f"Simple Interest: {simple_interest(2000, .025, 5)}")
print(f"Plan Finances: {plan_finances(2000, .025, 5, 5000)}")

