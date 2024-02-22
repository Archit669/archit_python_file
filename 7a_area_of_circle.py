# create a program that defines a function to calculate area of circle based on the radius entered by the user

import math

def calculate_circle_area(radius):
    return math.pi * radius**2

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_circle_area(radius)
    print("The area of the circle with radius", radius, "is:", round(area, 2))

if __name__ == "__main__":
    main()
