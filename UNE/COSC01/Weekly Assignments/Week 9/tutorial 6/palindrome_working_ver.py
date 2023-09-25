
def is_palindrome(s):
    # Base case: If the string has 0 or 1 characters, it's a palindrome.
    if len(s) <= 1:
        return True
    

    # Check if the first and last characters are the same.
    if s[0] == s[-1]:
        # Recursively check the substring without the first and last characters.
        return is_palindrome(s[1:-1])

    # If the first and last characters are different, it's not a palindrome.
    return False

# Example usage:



def is_palindrome_result(result):
    if is_palindrome(result):
        if len(result) <= 1:
            print(f"{result} is a palindrome")
        else:
            print(f"{result[1:-1]} is a Palindrome")

    else:
        print(f"{result} is not a palindrome")




is_palindrome_result("racecar")  # True
is_palindrome_result("hello")    # False