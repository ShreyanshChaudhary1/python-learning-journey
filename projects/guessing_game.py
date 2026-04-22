# mini project - number guessing game
import random  # random module for random number

secret = random.randint(1, 10)  # 1-10 random
guess_count = 0
guess_limit = 3  # sirf 3 chances

while guess_count < guess_limit:
    guess = int(input("Guess (1-10): "))
    guess_count += 1

    if guess == secret:
        print("You won!")
        break  # loop se bahar
else:
    # while ka else = loop complete hua bina break ke
    print(f"You lost! Number was {secret}")
