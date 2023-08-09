# Variables are set
max_passengers = 35 # Maximum bas seating capacity.
unhappy = 0         # Number of passengers left behind at a stop. No room.
total_passengers=0  # Totak number of passengers for route.
current_load = 0    # Current load of passegers on the bus.
stop = 0            # Counter stores the curent stop number.
available_seats = 0 # Available seats on the bus.
required = 0        # Number of seats availbale at each stop.
left_on_stop = 0    # Number of passengers left waiting at each stop.
number_of_stops = 0 # Number of stops along the route.
# get_on = int()
# get_off = int()
# start = int()
# route_number = int()




# Input qestion for bus route number.
# The input is validated as an integer. Letters / words not accepted.


while True:        
    route_number = input("What is the route number: ")
    try:
        route_number = int(route_number)
        break
    except ValueError:
        print("Please enter a number") 
print(f"Bus Route Number = {route_number}")




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





# Question for number of stops along bus route
# The input is validated as an integer. letters / words not accepted.

while True:
    number_of_stops = input("Please enter the number of stops on this route: " )
    try:
        number_of_stops = int(number_of_stops)
        break
    except ValueError:
        print("Please enter a number")
print(f"Number of stops on this route = {number_of_stops}")



# Starts bus stop loop.
# Question, How many waiting at stop. Stop number is retrieved from stop variable,
# incremented by 1 and displayed to the console.
while stop < number_of_stops:
    while True:
        get_on = input(f"How many waiting to get on at stop {stop + 1}?")
        try:
            get_on = int(get_on)
            break
        except ValueError:
            print("Please enter a number")
    get_on = int(get_on)
    print(f"Passengers waiting at bus stop {stop + 1} = {get_on}")


# Question, How many to depart at stop. Stop number is retrieved from stop variable,
# incremented by 1 and displayed to the console.

    while True:
        get_off =  input(f"How many to depart at bus stop {stop + 1}?")
        try:
            get_off = int(get_off)
            i =  current_load - get_off + get_on
            print(available_seats, max_passengers, current_load, get_off, get_on, unhappy)
            if i > max_passengers:
                print("Departing passengers cannot be larger than current passengers in the bus")
            else:
                break
        except ValueError:
            print("Please enter a number")

        get_off = int(get_off)

    print(f"Passengers waiting to depart bus at stop {stop + 1} = {get_off}")
   

 # Calculates bus seat availablity. Calculation is derived from passengers waiting / departing.   
   
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

       
 
 
    # print(f"Available capacity {available_seats}")
    
    

    
 






print(f"Unhappy customers (Total) = {unhappy}")
print(f"Total of all passengers for route = {total_passengers}")
if unhappy == 0:
    print("Customer satisfaction 100% guaranteed")
else:
    print(f"Ratio of happy to unhappy passengers{(total_passengers / unhappy) * 100}")
print("Thankyou for travelling with us today!!")

        


            
    
    


