

max_passengers = 35

unhappy = 0
total_passengers=0

current_load = 0

stop = 0


route_number = int(input("What is the route number: "))
print(f"Bus Route Number = {route_number}")
start = int(input("How many passengers waiting for bus at start of route? :"))
print(f"Bus passengers at start of route = {start}")
if start > max_passengers:
    print("Sorry, our maximum capacity is 35, some will need to wait for the  next bus")
    unhappy = start - max_passengers
    current_load = 35
    total_passengers = start

else:
    current_load = start
    total_passengers = start
    # print(f" = {current_load}")

number_of_stops = int(input("Please enter the number of stops on this route: " ))
print(f"Number of stops on this route = {number_of_stops}")




while stop < number_of_stops:
    get_on = int(input(f"How many waiting to get on at stop {stop + 1}?"))
    print(f"Passengers waiting at bus stop {stop + 1} = {get_on}")
    get_off = int(input(f"How many to depart at bus stop {stop + 1}?"))
    print(f"Passengers waiting to depart bus at stop {stop + 1} = {get_off}")
    # print(current_load)
    available_seats = max_passengers - current_load - get_off + get_on
 
    # print(f"Available capacity {available_seats}")
    
    

    
    


    if get_on <= available_seats:
        current_load = current_load + get_on - get_off
        print(f"Current load = {current_load}")
        total_passengers += get_on
        print(f"Available capacity {max_passengers - current_load}")
        stop += 1


    else:
        left_on_stop= get_on-available_seats
        unhappy += left_on_stop
        current_load += get_on-get_off-left_on_stop
        total_passengers += current_load
        available_seats = 0
        
        print(f"else unhappy passengers = {left_on_stop}")
        print(f"else Current load = {current_load}")
        print(f"else Available capacity = {available_seats}")
        stop += 1





print(f"Unhappy customers = {unhappy}")
print(f"Total passengers at end of route = {total_passengers}")
if unhappy == 0:
    print("Customer satisfaction 100% guaranteed")
else:
    print(f"Ratio of happy to unhappy passengers{(total_passengers / unhappy) * 100}")
print("Thankyou for travelling with us today!!")

        


            
    
    


