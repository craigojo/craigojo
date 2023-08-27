def is_palindrome(word):
    word_len = len(word)
    a = word[0].lower()
    b = word[-1].lower()


    if a == b:
        possible_palindrome = word[1:-1]
        return is_palindrome(possible_palindrome)
    elif word_len <=1:
        return False

possible_palindrome = input("Enter a word/phrase to check: ")

if is_palindrome(possible_palindrome):
    print(possible_palindrome, "is a palindrome")
else:
    print(possible_palindrome, "is not a palindrome")
