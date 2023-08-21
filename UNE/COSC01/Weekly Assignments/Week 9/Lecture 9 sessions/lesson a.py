# a= "1"
# int(a)

# s = str([1, 2.3, (4, 5), {6: 7}])
# print(s)
# type(s)

# age = 18
# "You are currently, %d years old" % age

# "You re currently %d years old. %d!" % (age, age)


# "In %d years you will be %d years" % (200, age + 200)


# "%(unit)s has %(students)d students" % {"unit": "COSC110", "students": 200}

# "%0+5g   %0+5g" % (1, -1)
# "%0+5g  %0+5g" % (1, -1)
# "%0+5g    %0+5g" % (1, -1)
# "%0+5g %0+5g" % (1, -1)
# "%0+5g   %0+5g" % (1, -1)


# "%s %d %d %s"  % ("Hello", 1, 3, "Craigo")


# name = "Fred"
# "{0} is {1} years old".format(name, age)
# "{0} is {1} years old".format(name, age)
# "{2} is {1} years old {2}".format(name, age, "Ok")
# "{2} is {2} years old {2}".format(name, age, "Ok")
# "{0} is {1:.2f} years old {2}".format(name, age, "Ok")


# f"{name} is {age}. In {3 * 5} years he will be {age + 5 * 3:.2f}"
# f"{name} is {s}. In {3 * 5} years he will be {age + 5 * 3:.2f}"

import os

def walk (dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isdir(path):
            walk(path)
        else:
            print(path)

walk(os.getcwd())




try:
    with open("hello.txt", "r") as file_in:
        for line in file_in:
            word = line.strip()

except IOError:
    print("IO error")






