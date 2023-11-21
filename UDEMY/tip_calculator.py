print("Welcome to the tip calculator\n\n")
bill = float(input("What was the total bill? \n$"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? \n"))
split = int(input("How many people will split the bill? \n"))

each = (bill + (bill * (tip/100))) /split

# print(f"Each person should pay: ${round(each, 2)}")

print(f"Each person should pay: ${each:.2f}")
