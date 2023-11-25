# print("Welcome to the Rollercoaster")
# height = int(input("What is your height in cm? "))

# cost = 0
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         cost += 5
#     if age <=18:
#         cost += 7
#     else:
#         cost += 12

#     photo = input("Would you like a photo? Y/N")
#     if photo == "Y":
#         print(f"Please pay ${cost + 3}")
#     else:
#         print(f"Please pay ${cost}")
# else:
#     (print("Sorry, you have to grow taller before you can ride"))




print("Welcome to the Rollercoaster")
height = int(input("What is your height in cm? "))

cost = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        cost += 5
        print("Child tickets are $5")
    if age <=18:
        cost += 7
        print("Youth tickets are $6")
    elif age >= 45 <= 55:
        cost += 0
        print("Everything is going to be ok. Havbe a free ride on us!")
    else:
        cost += 12
        print("Adult tickets are $12")
    photo = input("Would you like a photo? Y/N")
    if photo == "Y":
        cost += 3
    print(f"Please pay ${cost}")
else:
    (print("Sorry, you have to grow taller before you can ride"))