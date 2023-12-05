total = 0
for number in range(2, 1001, 2):
    total += number
print(total)

target = int(input()) # Number between 0 and 1000

# even_sum = 0
# for number in range(2, target + 1, 2):
#     even_sum += number
# print(even_sum)

alternative_sum = 0
for numbers in range(1, target + 1):
    if numbers % 2 == 0:
        alternative_sum += numbers
print(alternative_sum)