def factorial(n):
  if n < 0:
    return 1
  result = 1
  while n > 0:
      result = result * n
      n = n - 1
  return result
for i in range(-1, 5):
  print('Factorial of', i, 'is', factorial(i))