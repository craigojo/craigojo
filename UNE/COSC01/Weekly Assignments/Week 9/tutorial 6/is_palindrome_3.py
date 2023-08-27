def is_palindrome(word):
    word = word.lower()

    if len(word) <= 1:
        return True

    a = word[0]
    b = word[-1]

    if a == b:
        possible_palindrome = word[1:-1]
        print(possible_palindrome)
        return is_palindrome(possible_palindrome)
    else:
        return False

possible_palindrome = input("Enter a word/phrase to check: ")

if is_palindrome(possible_palindrome):
    print(possible_palindrome, "is a palindrome")
else:
    print(possible_palindrome, "is not a palindrome")
