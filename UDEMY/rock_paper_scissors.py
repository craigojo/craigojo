import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇




import random
random_integer = random.randint(0, 2)
rock_paper_scissors = str(input("Choose: rock, paper or scissors?")).lower()

if random_integer == 0:
    challenge = "rock"
    rock_rand = 1
elif random_integer == 1:
    challenge = "paper"
    paper_rand = 2
elif random_integer == 2:
    challenge = "scissors"
    scissors_rand = 3

if rock_paper_scissors == "rock":
   rock_challenge = 1
elif rock_paper_scissors == "paper":
   paper_challenge = 2
elif rock_paper_scissors == "scissors":
   paper_challenge = 3



if challenge == rock_paper_scissors:
    print("Draw!")
    heads_tails = "heads"
elif:
    heads_tails = "tails"
if challenge == heads_tails:
    print("You Win!")
else:
    print("You Loose!")


choice1 = input('Choose: Rock, paper or scissors?" \n').lower()
if choice1 == "rock":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")