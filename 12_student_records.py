# Create a program to enter student records [Rno., Name, Age] in a binary file. Also write a function to search for a particular Rollno in the file.

import pickle


class Student:

    def __init__(self, roll_no, name, age):
        self.roll_no = roll_no
        self.name = name
        self.age = age


def add_student_record(filename):
    try:
        with open(filename, "ab") as file:
            roll_no = int(input("Enter Roll No.: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))

            student = Student(roll_no, name, age)
            pickle.dump(student, file)
            print("Student record added successfully.")

    except Exception as e:
        print("Error:", e)


def search_student_record(filename, roll_no):
    try:
        with open(filename, "rb") as file:
            while True:
                try:
                    student = pickle.load(file)
                    if student.roll_no == roll_no:
                        print("Student Record Found:")
                        print("Roll No.:", student.roll_no)
                        print("Name:", student.name)
                        print("Age:", student.age)
                        return
                except EOFError:
                    break
        print("Student record not found for Roll No.:", roll_no)

    except FileNotFoundError:
        print("File not found.")


def main():
    filename = "student_records.bin"

    while True:
        print("\n1. Add Student Record")
        print("2. Search Student Record")
        print("3. Exit\n")
        choice = input("Enter your choice: ")

        print()

        if choice == "1":
            add_student_record(filename)
            print()
        elif choice == "2":
            roll_no = int(input("Enter Roll No. to search: "))
            print()
            search_student_record(filename, roll_no)
            print()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
            print()


if __name__ == "__main__":
    main()
