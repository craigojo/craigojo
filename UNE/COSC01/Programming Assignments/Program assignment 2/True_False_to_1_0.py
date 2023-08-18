bits = [False, True, False, False, True, True, True, False, False, False]
new_bite = []
super_bite = []

for b in bits:
    if b == True:
        new_bite.append(1)
    else:
        new_bite.append(0)


print(new_bite)

super_bite = [1 if b == True else 0 for b in bits]

print(super_bite)





