import turtle
import math
bob = turtle.Turtle()

# bob.lt(100)
# print(bob)
# turtle.mainloop()
def circle(t, r):
    circumference = 2 * math.pi * r
    n =50
    length = circumference /n
    polygon(t, n, length)













# def square(t, n, length):
    
#     angle = 360 / n
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)

# square(bob,10, 70)




# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(100)

# square(bob, 200)