list = "words.txt"
word_list = []
rejected_words = []
rejected_upper = []

def is_palindrome():
    with open(list, "r") as file:
        lines = file.readlines()
        for word in lines:
            word = word.strip()
            original = str(word)
            reversed_str = ''.join(reversed(original))

            if len(original) < 1:
                return False
            elif any(i.isupper() for i in word):
                rejected_upper.append(word)
            elif reversed_str != original:
                rejected_words.append(word)
            else:
                word_list.append(word)
            
                


is_palindrome(-1)

for i in word_list:

    print(i + "\n")

# print(rejected_upper)
# print(rejected_words)