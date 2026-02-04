import sys

from random import randint

def main():
    random_number = randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.\n")
    print("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n")

    sys.stdout.write("Enter your choice: ")
    user_choice = int(input().strip())

    if user_choice == 1:
        print("\nGreat! You have selected the Easy difficulty level.\nLet's start the game!")
        attempts = 10

    elif user_choice == 2:
        print("\nGreat! You have selected the Medium difficulty level.\nLet's start the game!")
        attempts = 5

    elif user_choice == 3:
        print("\nGreat! You have selected the Hard difficulty level.\nLet's start the game!\n")
        attempts = 3


    while True:
        sys.stdout.write("Enter your guess: ")
        user_guess = int(input().strip())

        if user_guess == random_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            print("Thank you for playing! Goodbye!")
            break

        else:
            attempts -= 1
            if user_guess < random_number:
                print(f"Incorrect! The number is greater than {user_guess}.\nYou have {attempts} attempts left.\n")
            elif user_guess > random_number:
                print(f"Incorrect! The number is less than {user_guess}.\nYou have {attempts} attempts left.\n")

            if attempts == 0:
                print("Sorry, you ran out of attempts.")
                print("Thank you for playing! Goodbye!")
                break

            continue

if __name__ == "__main__":
    main()