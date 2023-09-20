
epsilon = 0.001
square = float(input("Enter a value to find its square root: "))
a = float(square)
estimate = input("Enater an initaila estimate: ")
x = float(estimate)
while True:
    print(x)
    y = (x+a/x) / 2
    if abs(x - y) < epsilon:
        break
    x = y


print(x)






# square = float(input("Enter a value to find its square root: "))
# a = float(square)
# estimate = input("Enater an initaila estimate: ")
# x = float(estimate)
# while True:
#     print(x)
#     y = (x+a/x) / 2
#     if x == y:
#         break
#     x = y


# print(x)