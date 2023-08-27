def is_palindrome(word):
    word = word.lower()

    if len(word) <= 1:
        return True

    a = word[0]
    b = word[-1]

    if a != b:
        return False
    else:
        possible_palindrome = word[1:-1]
        return is_palindrome(possible_palindrome)

possible_palindrome = input("Enter a word/phrase to check: ")

if is_palindrome(possible_palindrome):
    print(possible_palindrome, "is a palindrome")
    print("New word:", possible_palindrome[1:-1])
else:
    print(possible_palindrome, "is not a palindrome")

