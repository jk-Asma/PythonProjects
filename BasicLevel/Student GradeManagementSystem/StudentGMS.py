# Project: Student Grade Management System
# Level: Basic Python
# Author:Asma
#
# Features:
# 1. Add Student
# 2. View All Students
# 3. Search Student
# 4. Update Marks
# 5. Delete Student
# 6. Exit
# ============================================================

# Dictionary to store student records
# Format:
# {
#   "Roll No": {
#       "name": "Student Name",
#       "marks": [90, 85, 80]
#   }
# }

students = {}

# Function to calculate average marks

def calculate_average(marks):
    return sum(marks) / len(marks)

# Function to calculate grade

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "Fail"

# Function to add a new student

def add_student():

    roll = input("Enter Roll Number: ")

    # Check if roll number already exists
    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")

    # Input marks for three subjects
    marks = []

    for i in range(3):
        mark = float(input(f"Enter Marks of Subject {i+1}: "))
        marks.append(mark)

    # Store student data
    students[roll] = {
        "name": name,
        "marks": marks
    }

    print("Student Added Successfully!\n")

# Function to display all students

def display_students():

    if not students:
        print("No student records found.\n")
        return

    print("\n========== STUDENT REPORT ==========")

    for roll, data in students.items():

        avg = calculate_average(data["marks"])
        grade = calculate_grade(avg)

        print("----------------------------------")
        print("Roll Number :", roll)
        print("Name        :", data["name"])
        print("Marks       :", data["marks"])
        print("Average     :", round(avg, 2))
        print("Grade       :", grade)

    print("----------------------------------\n")

# Function to search a student

def search_student():

    roll = input("Enter Roll Number to Search: ")

    if roll in students:

        data = students[roll]

        avg = calculate_average(data["marks"])
        grade = calculate_grade(avg)

        print("\nStudent Found")
        print("------------------------")
        print("Name :", data["name"])
        print("Marks:", data["marks"])
        print("Average:", round(avg, 2))
        print("Grade:", grade)

    else:
        print("Student Not Found!")

    print()

# Function to update marks

def update_marks():

    roll = input("Enter Roll Number: ")

    if roll not in students:
        print("Student Not Found!\n")
        return

    print("Enter New Marks")

    marks = []

    for i in range(3):
        mark = float(input(f"Subject {i+1}: "))
        marks.append(mark)

    students[roll]["marks"] = marks

    print("Marks Updated Successfully!\n")

# Function to delete a student

def delete_student():

    roll = input("Enter Roll Number: ")

    if roll in students:
        del students[roll]
        print("Student Deleted Successfully!\n")
    else:
        print("Student Not Found!\n")


# Main Program 

while True:

    print("===================================")
    print(" STUDENT GRADE MANAGEMENT SYSTEM")
    print("===================================")

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using the program!")
        break

    else:
        print("Invalid Choice! Please try again.\n")
