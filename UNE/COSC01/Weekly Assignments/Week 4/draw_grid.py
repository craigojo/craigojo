import time
def draw_grid(width, height):

    end_line = "+"
    internal_line = "|"
    for i in range(width):
        end_line = end_line + "-"
        
        internal_line = internal_line + " "
    end_line = end_line + "+"
    internal_line = internal_line + "|"
    time.sleep(0.2)
    print(end_line)

    for i in range(height):
        print(internal_line)

    print(end_line)


draw_grid(20, 4)



