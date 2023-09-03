def any_lowercase(s):
    for c in s:
        c = c.islower()
    return c

result = any_lowercase("C")
print(result)




def any_lowercase1(s):
  for c in s:
    if 'c'.islower():
      return 'True'
    else:
      return 'False'
      
result = any_lowercase1("barry")
print(result)



def any_lowercase1(s):
  for c in s:
    if flag.islower():
    return flag

      
result = any_lowercase1("barry")
print(result)


def any_lowercase5(s):
  for c in s:
    if not c.islower():
      return False
  return True


def any_lowercase4(s):
  flag = False
  for c in s:
    flag = flag or c.islower()
  return flag