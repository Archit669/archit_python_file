#create a program that calculates the factorial of a number entered by the user using while loop

num = int(input("enter your number: "))
fact = 1

i = 1
while (i <= num):
    fact *= i
    i+=1

print("factorial of a number is :", fact)