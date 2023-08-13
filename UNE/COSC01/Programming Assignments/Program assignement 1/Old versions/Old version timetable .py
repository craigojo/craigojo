# Question for How many passengers will board the bus at start of bus route
# The input is validated as an integer. letters / words not accepted.

while True:  
    start = input("How many passengers waiting for bus at start of route? :")
    try:
        start = int(start)
        break
    except ValueError:
        print("Please enter a number")
print(f"Bus passengers at start of route = {start}")

# Accepts or rejects passegers at start of route. Maxiumum seats, 35. Stores overflow in variable unhappy
if start > max_passengers:
    unhappy = start - max_passengers
    current_load = 35
    total_passengers = start
    print(f"Sorry, our maximum capacity is 35, {unhappy} will need to wait for the next bus")



else:
    current_load = start
    total_passengers = start




if get_on > get_off:
        required = get_on - get_off
        if current_load + required > max_passengers:
            left_on_stop = required - (max_passengers - current_load)
            print('1')
            unhappy += left_on_stop
            current_load = max_passengers ##
            total_passengers += required - left_on_stop
            stop += 1
            print(f"else unhappy passengers at stop {stop} = {left_on_stop}")
            print(f"else Current load = {current_load}")
            print(f"else Available capacity = {available_seats}")
            print(available_seats, max_passengers, current_load, get_off, get_on, unhappy)
        else:

            total_passengers += get_on
            current_load += get_on - get_off
            print(2)
            
            available_seats = max_passengers - current_load
            
            print(available_seats, max_passengers, current_load, get_off, get_on, unhappy)
            print(f"else unhappy passengers at stop {stop} = {left_on_stop}")
            print(f"else Current load = {current_load}")
            print(f"else Available capacity = {available_seats}")
            stop += 1

        
    elif get_off >= get_on:
        print(3)
        required = get_off - get_on

        current_load = current_load - required
        print(f"Current load = {current_load}")
        total_passengers += get_on
        available_seats = max_passengers - current_load
        print(f"Available capacity {available_seats}")
        stop += 1
        print(available_seats, max_passengers, current_load, get_off, get_on, unhappy)
