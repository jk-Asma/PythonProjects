# Project Name : Number Guessing Game
# Level        : Basic Python
# Author       : Asma

# Features:
# 1. Computer generates a random number.
# 2. User guesses the number.
# 3. Displays hints (Too High / Too Low).
# 4. Counts the number of attempts.
# 5. Allows the user to play again.


# Import random module
import random

# Function to play the game
def play_game():

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Variable to count attempts
    attempts = 0

    print("\n====================================")
    print("  WELCOME TO NUMBER GUESSING GAME  ")
    print("====================================")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!\n")

    # Loop until the correct number is guessed
    while True:

        try:
            # Take input from the user
            guess = int(input("Enter your guess: "))

            # Increase attempt count
            attempts += 1

            # Compare the guess with the secret number
            if guess < secret_number:
                print("Too Low! Try Again.\n")

            elif guess > secret_number:
                print("Too High! Try Again.\n")

            else:
                print("\nCongratulations!")
                print(f"You guessed the correct number: {secret_number}")
                print(f"Total Attempts: {attempts}")

                # Display performance message
                if attempts <= 3:
                    print("Excellent! You're a genius! ")
                elif attempts <= 7:
                    print("Great Job! ")
                elif attempts <= 10:
                    print("Good! Keep practicing.")
                else:
                    print("You got it! Better luck next time.")

                # Exit the loop
                break

        except ValueError:
            print("Invalid Input! Please enter a valid number.\n")

# Main Program

while True:

    # Start the game
    play_game()

    # Ask the user if they want to play again
    choice = input("\nDo you want to play again? (Y/N): ").upper()

    if choice != "Y":
        print("\nThank you for playing the Number Guessing Game!")
        break
