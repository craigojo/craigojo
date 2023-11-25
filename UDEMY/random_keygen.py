import random
import string
random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)


random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
print(random_string)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")