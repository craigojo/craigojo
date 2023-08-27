def is_palindrome(word):
    original = str(word)

    reversed_str = ''.join(reversed(original))


    if len(original) < 1:
        return False
    elif any(i.isupper() for i in word):
        if word:
            return False
    elif reversed_str != original:

        return is_palindrome
    else:

       return is_palindrome


    



possible_palindrome = input("Enter a word/phrase to check: ")

if is_palindrome(possible_palindrome):
    print(possible_palindrome, "is a palindrome")
else:
    print(possible_palindrome, "is not a palindrome")
