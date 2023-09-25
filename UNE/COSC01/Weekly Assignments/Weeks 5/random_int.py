import random

target = random.randint(1, 20)

guess = 0
while guess != target:
  guess = int(input("Enter a guess between 1 and 20 (inclusive): "))
  if guess > target:
    print("You guessed too high!")
  elif guess < target:
    print("You guessed too low!")

print("Congratulations!")
