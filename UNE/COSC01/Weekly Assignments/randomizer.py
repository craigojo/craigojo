
import random

i = random.randit(1, 99)

guess = int(input("Enter an integer from 1 to 99: "))

while True:
        if guess < i:
                print("Guess is low")
                guess = int(input("Enter an integer form 1 to 99: "))
        elif guess > i:
                print("Guess is high")
                guess(input("Enter an integer from 1 to 99: "))
        else:
                print("You guessed it right!! Goodbye :)")
                break


