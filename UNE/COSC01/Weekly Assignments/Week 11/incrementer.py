
def make_incremeter(n):
    return lambda x: x + n

f = make_incremeter(1)
g = make_incremeter(7)
print(f(7), g(7))
