#create a program to take string from user and reverse a string

str = input("enter your string: ")

newStr = ""

for i in range(len(str)-1 , -1, -1):
    newStr += str[i]

print("reverse of string is : ", newStr)