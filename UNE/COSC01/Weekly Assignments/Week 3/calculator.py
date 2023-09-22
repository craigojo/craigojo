#!/usr/bin/env python3
name = input("Please enter your name: ")
print("Hello " + name + "!\n")

first = input("Please enter the first number: ")
first = int(first)

second = input("Please enter the second number: ")
second = int(second)

if first < second:
  print(first, "is less than", second)
elif second < first:
  print(first, "is greater than", second)
else:
  print(first, "is equal to", second)
  print("Did you do that on purpose?")

# average = (first + second) / 2
# print("The average of the two numbers is: " + str(average))



average = int((first + second) / 2)


print("The average of the two numbers is: " + (f"{average}"))
print("The average of the two numbers is: " + str(average))