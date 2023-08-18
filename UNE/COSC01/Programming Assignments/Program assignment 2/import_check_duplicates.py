file = open("routes.txt", "r")
read = file.readlines()


print(read)

modified = []

for line in read:
    if line not in modified:
        modified.append(line.strip())

print(modified)




# to check for duplicates

# if line not in modified