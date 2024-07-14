# Exercise 1: List Manipulation

# Create a list called fruits containing the following fruits: apple, banana, cherry, date.
# Add "elderberry" to the end of the list.
# Remove "banana" from the list.
# Sort the list in alphabetical order.
# Print the list.

fruits_list = ['apple', 'date', 'banana', 'cherry']
fruits_list.append('elderberry')
del fruits_list[2]
fruits_list.sort()
print(fruits_list)

# Exercise 2: Dictionary Basics

# Create a dictionary called student with the following key-value pairs:
# name: John Doe
# age: 25
# major: Computer Science
# Change the value of 'major' to "Electrical Engineering".
# Add a new key-value pair: 'year' with a value of 'Senior'.
# Print out the keys in the dictionary.
# Print out the values in the dictionary.

student_dict = {'name': 'John Doe', 'age': '25', 'major': 'Computer Science'}
student_dict['major'] = "Electrical Engineering"

new_key = 'year'
new_value = 'Senior'

updated_dict = {**student_dict, new_key: new_value}
print(updated_dict)

# Exercise 3: List of Dictionaries

# Create a list of dictionaries, where each dictionary represents a book
# and has the following keys: title, author, and year.
# Add at least 3 books to your list.
# Print the title of the second book in the list.
# Print the year the third book was published.
# Iterate over the list and print out each book's title and author.

books = [
    {'title': 'Harry Potter and the Sorcerors Stone', 'author': 'J.K. Rowling', 'year': 1997}, 
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960}, 
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925}
]
print("Title of the second book:", books[1]["title"])
print("Year the the third book was published:", books [2]['year'])

for book in books:
    print(f"Title: {book['title']}, Author: {book['author']}")

print("")

# Exercise 4: Dictionary containing a List

# Create a dictionary called courses where the keys are the names of courses
# (e.g., "math", "history", "chemistry") and the values are lists of student
# names enrolled in each course. Initialize every course with a list of some 
# random names of your choosing (ie, a list of strings). Then complete the
# following using methods/functions:
# Add 5 students to "math".
# Remove the third student from "history".
# Print out the students in "chemistry".
# Add a new course "physics" with a list of 4 students.

courses = {
    'math': ['Tom', 'Jerry', 'Cat', 'Mouse', 'Carlos'], 
    'history': ['Tom', 'Jerry', 'Cat', 'Mouse', 'Carlos'],
    'chemistry': ['Tom', 'Jerry', 'Cat', 'Mouse', 'Carlos']
    }

courses['math'].extend(["Jake", "Karen", "Leo", "Mia", "Nina"])
courses['history'].pop(2)
print("Students in chemistry:", courses['chemistry'])

courses['Anatomy and Physiology'] = ['Zach', 'Illeana', 'Veronica', 'Carlos', 'Gil']
print("Courses dictionary:", courses)

# new_key = 'physics'
# new_value = ['Tom', 'Jerry', 'Cat', 'Mouse']
# updated_courses = {**courses, new_key: new_value}
# print(updated_courses)