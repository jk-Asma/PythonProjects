# Project Name : Simple Calculator
# Author       : Asma

# Features:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Modulus
# 6. Power
# 7. Floor Division
# 8. Exit
# ------------------------------------------------------------

 
# Function for Addition
def add(a, b):
    return a + b

# Function for Subtraction
def subtract(a, b):
    return a - b

# Function for Multiplication
def multiply(a, b):
    return a * b

# Function for Division
def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

# Function for Modulus
def modulus(a, b):
    if b == 0:
        return "Error! Modulus by zero is not allowed."
    return a % b

# Function for Power
def power(a, b):
    return a ** b

# Function for Floor Division
def floor_division(a, b):
    if b == 0:
        return "Error! Floor division by zero is not allowed."
    return a // b

# Main Program

while True:

    # Display menu
    print("\n====================================")
    print("        SIMPLE CALCULATOR")
    print("====================================")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Floor Division (//)")
    print("8. Exit")

    # Take user choice
    choice = input("Enter your choice (1-8): ")

    # Exit program
    if choice == "8":
        print("\nThank you for using the Calculator!")
        break

    # Validate menu choice
    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid choice! Please try again.")
        continue

    # Take numbers from the user
    try:
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    # Perform selected operation
    if choice == "1":
        result = add(num1, num2)
        print(f"\nResult = {num1} + {num2} = {result}")

    elif choice == "2":
        result = subtract(num1, num2)
        print(f"\nResult = {num1} - {num2} = {result}")

    elif choice == "3":
        result = multiply(num1, num2)
        print(f"\nResult = {num1} × {num2} = {result}")

    elif choice == "4":
        result = divide(num1, num2)
        print(f"\nResult = {result}")

    elif choice == "5":
        result = modulus(num1, num2)
        print(f"\nResult = {result}")

    elif choice == "6":
        result = power(num1, num2)
        print(f"\nResult = {num1}^{num2} = {result}")

    elif choice == "7":
        result = floor_division(num1, num2)
        print(f"\nResult = {result}")

    # Ask user if they want to continue
    print("\nCalculation Completed Successfully!")
