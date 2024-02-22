# Create a program that defines a function to calculate the area of a rectangle based on sides entered by the user.

def calculate_rectangle_area(length, width):
    return length * width

def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = calculate_rectangle_area(length, width)
    print("The area of the rectangle with length", length, "and width", width, "is:", area)

if __name__ == "__main__":
    main()
