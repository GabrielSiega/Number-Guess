import random

def guess_number():
    correct_number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    message = "Congratulations! Your guess is correct." if guess == correct_number else f"Sorry, the correct number was {correct_number}. You guessed wrong."
    print(message)

guess_number()
