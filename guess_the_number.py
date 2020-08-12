#Guess The Number
#Thomas McLaughlin
#8/12/2020

import random

number = random.randint(1,1000)
attempts = 0
guess = 0

while guess != number:
    guess = input("Guess an integer 1-1000: ")
    guess = int(guess)
    if guess > 1000 or guess < 1:
        print("Guess out of range, please try again")
    elif guess == number:
        print("CONGRATS YOU WIN, THE NUMBER IS: " + str(number))
        break
    elif guess > number:
        print("Your guess is higher than the number.")
        attempts += 1
    elif guess < number:
        print("Your guess is lower than the number.")
        attempts += 1

print("You guessed the correct number in " + str(attempts) + " attempts.")