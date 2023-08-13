
import random

i = random.randint(1, 8)

guess = int(input("Enter an integer from 1 to 99: "))

while guess != i:
        if guess < i:
                print("Guess is low")
                guess = int(input("Enter an integer form 1 to 99: "))
        elif guess > i:
                print("Guess is high")
                guess = int(input("Enter an integer from 1 to 99: "))

print("You guessed it right!! Goodbye :)")



