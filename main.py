import random

number = random.randint(1, 100)
attempts = 0

print("I chose a number between 1 and 100.")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess == number:
        print(f"Correct! You won in {attempts} attempts.")
        break
    if guess < number:
        print("Too low.")
    else:
        print("Too high.")
