import random
random_integer = random.randint(0, 1)
heads_tails = str(input("Heads or tails? H or T")).lower()

if random_integer == 0:
    challenge = "heads"
else:
    challenge = "tails"

if heads_tails == "heads" or heads_tails =="t":
    heads_tails = "heads"
else:
    heads_tails = "tails"
if challenge == heads_tails:
    print("You Win!")
else:
    print("You Loose!")
    