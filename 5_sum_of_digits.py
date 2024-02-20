#write a program that input a number from user and calculate the sum of digits

num = int(input("enter a number: "))

sum = 0

while (num > 0):
    sum += num % 10
    num = num // 10

print("sum of digits of a given number is " , sum)