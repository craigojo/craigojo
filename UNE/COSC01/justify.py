value = input("Enter string to justify: ")
def right_justify(input_string):
    i = len(input_string)
    if i <= 79:
        spaces = 80 - i
        spaces = int(spaces)

        print(spaces * ' ' + input_string)
    else:
        print(input_string)



value = input("Enter string to justify: ")
right_justify(value)