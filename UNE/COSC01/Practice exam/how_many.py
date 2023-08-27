def func(n):

    if n < 1:
        return n
    if n % 2 == 1:

        return func(n - 1)

    return func(n // 2)


func(5)
