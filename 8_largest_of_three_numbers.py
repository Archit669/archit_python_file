# Write a program to find largest of three numbers.

def find_largest(num1, num2, num3):
    if num1 >= num2:
        if num1 >= num3:
            return num1
        else:
            return num3
    else:
        if num2 >= num3:
            return num2
        else:
            return num3

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    
    largest = find_largest(num1, num2, num3)
    print("The largest number among", num1, ",", num2, ", and", num3, "is:", largest)

if __name__ == "__main__":
    main()
