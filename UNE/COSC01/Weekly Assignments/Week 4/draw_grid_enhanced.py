

def draw_grid(width, height):
    end_line = '+'
    internal_line = '|'

    for i in range(width):
        end_line = end_line + '-'
        internal_line = internal_line + ' '
    end_line = end_line + '+'
    internal_line = internal_line + '|'
    print(end_line)

    for i in range(height):
        print(internal_line)

    print(end_line)

while True:
        a = int(input("enter a value for width"))
        b = int(input("enter a value for height"))

        draw_grid(a, b)

        again = str(input("Play again?"))

        if again.upper() != 'Y':
            break









    

