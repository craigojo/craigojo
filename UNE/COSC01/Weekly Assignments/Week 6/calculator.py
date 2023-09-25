
def add(x, y):
    add = x + y
    return add

def sub(x, y):
    sub = x - y
    return sub


def mul(x, y):
    mul = x * y
    return mul

def div(x, y):
    div = x / y
    return div
    
while True:
    try:
        num_1 = int(input("Enter value for x: " ))            
    except ValueError:
        print("Try again")
    else:
        print(f'You entered: {num_1}')
        break
        
while True:
    try:
        num_2 = int(input("Enter value for y: "))
    except ValueError:
        print("Try again")
    else:
        print(f'You entered: {num_2}')
        break

if num_2 > num_1:
    val_a = mul(num_1, num_2)
    val_b = add(num_1, num_2)
    calculate_strange_value = val_a * val_b
    print(f'sTranGe  ValUe = {calculate_strange_value}')

elif num_1 > num_2:
    val_a = div(num_1, num_2)
    val_b = sub(num_1, num_2)
    calculate_strange_value = int(val_a * val_b)
    print(f'sTranGe  ValUe = {calculate_strange_value}')

elif num_1 == num_2:
    print("sTranGe  ValUe = 1")










