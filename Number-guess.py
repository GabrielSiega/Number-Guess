import random

def guess_number():
    # Generate a random number between 1 and 10
    correct_number = random.randint(1, 10)

    # Get user's guess
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Check if the guess is correct
    if guess == correct_number:
        print("Congratulations! Your guess is correct.")
    else:
        print(f"Sorry, the correct number was {correct_number}. You guessed wrong.")

# Call the function to start the game
guess_number()
