import time

from random import randint

def select_difficulty():
    print("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n")
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("\nGreat! You have selected the Easy difficulty level.")
            return 10
        elif choice == 2:
            print("\nGreat! You have selected the Medium difficulty level.")
            return 5
        elif choice == 3:
            print("\nGreat! You have selected the Hard difficulty level.")
            return 3
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def play_game():
    random_number = randint(1, 100)
    chances = select_difficulty()
    attempts = 0
    start_time = time.time()

    print("Let's start the game!\n")

    while chances > 0:
        try:
            guess = int(input("Enter your guess: ").strip())
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess == random_number:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            print(f"Time taken: {elapsed_time:.2f} seconds.")
            return attempts
        else:
            chances -= 1
            if guess < random_number:
                print(f"Incorrect! The number is greater than {guess}.\nYou have {chances} attempts left.\n")
            elif guess > random_number:
                print(f"Incorrect! The number is less than {guess}.\nYou have {chances} attempts left.\n")

    print(f"Sorry, you've run out of chances. The correct number was {random_number}.")
    return attempts

def main():
    while True:
        print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
        attempts = play_game()

        play_again = input("\nDo you want to play again? (yes or no): ").strip().lower()

        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()