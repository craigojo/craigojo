def find(word, letter):
    index=0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

def count(word, letter):
    count = 0
    index = 0
    while index < len(word):
        if word[index] == letter:
            count += 1
        index += 1
    return count

print(count("Hello", "e"))
print(count("Hello", "z"))
print(count("Goodbye", "o"))
