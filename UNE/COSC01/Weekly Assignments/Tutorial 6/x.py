# def add(x, y):
#   return x + y

# def sub(x, y):
#   return x - y

# def mul(x, y):
#   return x * y

# def div(x, y):
#   return x / Y

# def calculate_strange_value(x, y):
#   if y > x:
#     return mul(x, y) * add(x, y)
#   elif x > y:
#     return div(x, y) * sub(x, y)
#   else:
#     return 1

# def is_valid_positive_integer_input(value):
#   if not isinstance(value, (str, int)):
#     return False
#   try:
#     value = int(value)
#   except (TypeError, ValueError):
#     return False
#   return value > 0




def main():
  x = input("Enter a positive integer: ")
  while not is_valid_positive_integer_input(x):
    x = input("Enter a positive integer: ")
  x = int(x)

#   y = input("Enter a positive integer: ")
#   while not is_valid_positive_integer_input(y):
#     y = input("Enter a positive integer: ")
#   y = int(y)

#   print(calculate_strange_value(x, y))

# if __name__ == "__main__":
#   main()