import math

def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area



# We are looking for the area of a circle

r = int(input("Enter the radius of the circle: "))

print(f"the area of the circle with radius {r} is:", math.pi * r**2)

# We are looking for the area of a triangle

b = int(input(f"Enter the base of the triangle: "))
h = int(input(f"Enter the height of the triangle: "))

print(f"The area of the triangle with base {b} and height {h} is:", (0.5 * b * h))

# We are looking for the area of a rectangle

x = int(input("Enter the length of the rectangle: "))
y = int(input("Enter the width of the rectangle: "))

print(f"The area of the rectangle with lenth {x} and width {y} is:", (x * y))
