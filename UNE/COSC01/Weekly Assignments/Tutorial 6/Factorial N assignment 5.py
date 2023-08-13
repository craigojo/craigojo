def factorial(n):

    

  result = 1
  while n != 0:
    result = result * n
    n = n - 1
    
  return result



for i in range(-1, 5):
  if i < 1:
    pass
  else:
    print('Factorial of', i, 'is', factorial(i))