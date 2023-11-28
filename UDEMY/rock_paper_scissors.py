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
    rand = 1
elif random_integer == 1:
    challenge = "paper"
    rand = 2
elif random_integer == 2:
    challenge = "scissors"
    rand = 3

if rock_paper_scissors == "rock":
   input_challenge = 1
elif rock_paper_scissors == "paper":
   input_challenge = 2
elif rock_paper_scissors == "scissors":
   input_challenge = 3



if challenge == rock_paper_scissors:
    print("Draw!")

elif  rand < input_challenge < 3 :
    print("You Win!")
if challenge == heads_tails:
    print("You Win!")
else:
    print("You Loose!")



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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end