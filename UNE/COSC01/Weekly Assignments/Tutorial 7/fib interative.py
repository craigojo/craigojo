def fibonacci_iterative(n):
    a = 1
    b = 1
    for i in range(n):
        a, b = b, a + b
        print(a)
        print(b)
    return a

fibonacci_iterative(5)