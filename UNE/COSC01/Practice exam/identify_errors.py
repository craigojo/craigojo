start = input("Enter a value: ")
n = int(start)
while n != 1:
    print (n)
    if n % 2 == 0: # n even
        n = n // 2
    else: # n odd
        n = 3 * n + 1