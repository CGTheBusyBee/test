import math

def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area



# # We are looking for the area of a circle

# r = int(input("Enter the radius of the circle: "))

# print(f"the area of the circle with radius {r} is:", math.pi * r**2)

# # We are looking for the area of a triangle

# b = int(input(f"Enter the base of the triangle: "))
# h = int(input(f"Enter the height of the triangle: "))

# print(f"The area of the triangle with base {b} and height {h} is:", (0.5 * b * h))

# # We are looking for the area of a rectangle

# x = int(input("Enter the length of the rectangle: "))
# y = int(input("Enter the width of the rectangle: "))

# print(f"The area of the rectangle with length {x} and width {y} is:", (x * y))



# Define the rectangle, circle, and triangle area calculations as functions.
# Create a function named square_perimeter that takes the side length of a
# square and returns its perimeter.

# Write a function named circle_details that takes the radius of a circle
# as its only argument and prints out both the circumference and the area
# of the circle.

# Write a function named geometry that takes the side length of a square
# and the radius of a circle. The function should print which shape has a
# larger perimeter/circumference and which shape has a larger area.

def rectangle_area(length, width):
    area = length * width
    return area

def circle_area(radius):
    area = math.pi * radius**2
    return area

def triangle_area(half, base, height):
    area = half * base * height
    return area

def square_area(side_length):
    area = side_length * side_length
    return area

def square_perimeter(side_length):
    perimeter = side_length * 4
    return perimeter

def circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

def circle_details(radius):
    print(f"Circumference: {circumference(radius)}")
    print(f"Area: {circle_area(radius)}")

def geometry(side_length, circle_radius):
    perimeter = square_perimeter(side_length)
    circum = circumference(circle_radius)
    if perimeter > circum:
        print("Square has a larger perimeter.")
        print("Square has a larger area.")
    else:
        print("Circle has a larger circumference.")
        print("Circle has a larger area.")


print(f"Square perimeter: {square_perimeter(10)}")
print(f"Square area: {square_area(10)}")
circle_details(5)
geometry(10, 5)