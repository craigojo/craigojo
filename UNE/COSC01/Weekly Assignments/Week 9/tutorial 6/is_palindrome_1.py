def is_palindrome(i):
    original = str(i)
    reversed_str = ' '.join(reversed(original))
    print(reversed_str)

    if len(i) <= 1:
        return False
    elif reversed_str != original:
        return False
    else:
       return True

print(is_palindrome("anna"))
