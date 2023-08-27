def is_palindrome(word):
    not_rev = word.lower()

    rev = ''.join(reversed(word.lower()))

    if len(word) <= 1:
        return False
    
    elif rev != not_rev:

        return False
    
    else:
       return True
    

print (is_palindrome("anna"))