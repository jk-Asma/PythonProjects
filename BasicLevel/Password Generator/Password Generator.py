# Project Name : Password Generator
# Level        : Basic Python
# Author       : Asma

# Features:
# 1. User chooses password length
# 2. Include uppercase letters
# 3. Include lowercase letters
# 4. Include numbers
# 5. Include special characters
# 6. Generate random secure password


# Import required modules
import random
import string

# Function to generate password
def generate_password(length, use_upper, use_lower, use_digits, use_symbols):

    # Empty string to store all selected characters
    characters = ""

    # Add uppercase letters if user chooses Yes
    if use_upper:
        characters += string.ascii_uppercase

    # Add lowercase letters if user chooses Yes
    if use_lower:
        characters += string.ascii_lowercase

    # Add digits if user chooses Yes
    if use_digits:
        characters += string.digits

    # Add special symbols if user chooses Yes
    if use_symbols:
        characters += string.punctuation

    # Check whether at least one option is selected
    if characters == "":
        return "Error! Please select at least one character type."

    # Generate password
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password



# Main Program

print("======================================")
print("       PASSWORD GENERATOR")
print("======================================")

# Ask user for password length
length = int(input("Enter Password Length: "))

# Ask user which characters to include
upper = input("Include Uppercase Letters? (Y/N): ").upper()
lower = input("Include Lowercase Letters? (Y/N): ").upper()
digits = input("Include Numbers? (Y/N): ").upper()
symbols = input("Include Special Characters? (Y/N): ").upper()

# Convert Y/N into True/False
use_upper = upper == "Y"
use_lower = lower == "Y"
use_digits = digits == "Y"
use_symbols = symbols == "Y"

# Generate password
password = generate_password(
    length,
    use_upper,
    use_lower,
    use_digits,
    use_symbols
)

# Display generated password
print("")
print("Generated Password:")
print(password)

