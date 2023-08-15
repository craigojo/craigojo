
def is_valid_positive_integer_input(value):
  if not isinstance(value, (str, int)):
    return False
  try:
    value = int(value)
  except (TypeError, ValueError):
    return False
  return value > 0


def is_valid_route_number(value):
  if value < 3:
    return False
  else:
    return True
  







def main():
  route_number = input("Please enter a route number: ")
  while not is_valid_positive_integer_input(route_number):
    route_number = input("Enter a positive integer: ")
  while not is_valid_route_number(route_number):
    route_number = input("Enter a value, route must have minimum 3 stops ")
  route_number = int(route_number)

  number_of_stops = input("Please enter the number of stops on this route: " )
  while not is_valid_positive_integer_input(number_of_stops):
    number_of_stops = input("Enter a positive integer: ")
  number_of_stops = int(number_of_stops)
  
  number_of_stops = input("Enter a positive integer: ")
  while not is_valid_positive_integer_input(y):
    number_of_stops = input("Enter a positive integer: ")
  number_of_stops = int(number_of_stops)

  main()

