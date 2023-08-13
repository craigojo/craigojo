def find(word, letter):
    index=0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1


print(find("Hello", "e"))
print(find("Hello", "z"))
print(find("Hello", "o"))
