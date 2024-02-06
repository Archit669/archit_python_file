#create a program that calculates the factorial of a number entered by the user using for loop

num = int(input("enter your number: "))
fact = 1

for i in range(1, num+1):
    fact *= i

print("factorial of a number is :", fact)