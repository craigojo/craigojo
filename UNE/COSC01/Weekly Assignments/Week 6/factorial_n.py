def factorial(n):
    product = 1
    while n > 0:
        product = product * n
        n = n - 1
    return product

factorial(5)