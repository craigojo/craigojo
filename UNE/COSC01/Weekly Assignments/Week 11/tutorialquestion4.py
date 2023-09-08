# Implement functions named linear and bisection, each of which take a list and a target value as parameters. 
# linear should perform a linear search, and bisection a bisection search. 
# They should each return the index of the target value if it is in the list, or None if it is not.


def linear(search_list, target):
  for i in range(len(search_list)):
    if target == search_list[i]:
      return i
  return None

def bisection(search_list, target):
  # Note: This requires search list to be sorted
  lower = 0
  upper = len(search_list) - 1

  # Search while it is still possible the target is within range
  while lower <= upper:
    # Check the midpoint
    mid = lower + (upper - lower) / 2
    if target == search_list[mid]:
      # We found it!
      return mid
    if target < search_list[mid]:
      # If the target is in the list, it must be in the left half
      upper = mid - 1
    else:
      # If the target is in the list, it must be in the right half
      lower = mid + 1

  # target mustn't be in list
  return None