# create a program that prompts a user for their age and tells them if they can vote in the next election

age = int(input("Enter your age: "))

if (age < 18):
    print("You cannot vote in the next election")
else: 
    print("You can vote in the next election")