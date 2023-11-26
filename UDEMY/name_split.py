import random
names_string = ("a, b, c, d, e ,f ,g ,h")
names = names_string.split(", ")
name_index = random.randint(0, len(names) - 1)
pay = names[name_index]
print(f"{pay} is going to pay for the meal today!")