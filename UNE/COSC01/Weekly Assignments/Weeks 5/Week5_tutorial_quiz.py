def any_lowercase1(s):
  for c in s:
    if c.islower():
      return True
    else:
      return False

# The above function checks to see if the first character of the string is lowercase.


def any_lowercase2(s):
  for c in s:
    if 'c'.islower():
      return 'True'
    else:
      return 'False'

# The above function always returns True if a non-empty string is passed in, 
# because the character 'c' is always lowercase. 
# If the parameter is an empty string, the result is None



def any_lowercase3(s):
  for c in s:
    flag = c.islower()
  return flag

#The above function overwrites the value of flag for each character, 
# so only returns True if the last character in the string is lowercase.





def any_lowercase4(s):
  flag = False
  for c in s:
    flag = flag or c.islower()
  return flag

any_lowercase4("QWEER")

# The above function checks to see if the string contains at least one lowercase character.





def any_lowercase5(s):
  for c in s:
    if not c.islower():
      return False
  return True



# The above function checks to see if the entire string is lowercase.




available = {"pen": 3, "pencil": 5, "eraser": 2, "paper": 10}
total = 0
for key in available:
    total += available[key]
print(total)


# The available dictionary specifies the number of each item that is available.
#  Write a program that loops through all the keys in the available dictionary to help determine the total number of items available 
# (e.g. in the given case, there are 3 pens, 5 pencils, 2 erasers, and 10 papers, so your program should output 20). 
# Your program should display a count of the total number
#  of items specified in the available dictionary even if you modify the keys/values in
#  the dictionary.