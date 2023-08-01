def factorial(n):
  result = 1
  n=1

  while n != 0:
    n = n - 1
    result = result * n
    return result

for i in range(-1, 5):
  print('Factorial of', i, 'is', factorial(i))