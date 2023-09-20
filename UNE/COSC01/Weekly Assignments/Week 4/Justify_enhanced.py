#!/usr/bin/env python3
while True:
    value = str(input("Input a string"))

    def justify_right(input_string):

        i = (int(len(input_string)))

        if i <= 79:
            spaces = 80 - i
            print(spaces * " " + input_string)

        else:
            print(input_string)

    justify_right(value)

    again = input("Play again? Y/N")
    if again.upper() != 'Y':
        break