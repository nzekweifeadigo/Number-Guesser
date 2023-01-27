import random

# Generate a random number
number = random.randint(1, 100)

# Ask the user to guess the number
guess = int(input("Guess the number between 1 and 100: "))

# Keep asking the user to guess the number until they get it right
while guess != number:
    if guess < number:
        print("Too low! Guess again.")
    else:
        print("Too high! Guess again.")
    guess = int(input("Guess the number between 1 and 100: "))

# Congratulate the user on guessing the number
print("Congratulations! You guessed the number.")
