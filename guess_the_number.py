import random

print("Welcome to the Guess the Number Game!")

# The computer picks a random number
secret_number = random.randint(1, 100)

attempts = 0
guess = 0

while guess != secret_number:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts}tries.")