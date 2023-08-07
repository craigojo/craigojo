

max_passengers = 35
unhappy = 0
total_passengers=0
current_load = 0
stop = 0
available_seats = 0
required = 0
left_on_stop = 0

route_number = int(input("What is the route number: "))
print("Please enter a valid number")

print(f"Bus Route Number = {route_number}")
start = int(input("How many passengers waiting for bus at start of route? :"))
print(f"Bus passengers at start of route = {start}")
if start > max_passengers:

    unhappy = start - max_passengers
    current_load = 35
    total_passengers = start
    print(f"Sorry, our maximum capacity is 35, {unhappy} will need to wait for the  next bus")


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
    
    
    if get_on > get_off:
        required = get_on - get_off
        if current_load + required > max_passengers:
            left_on_stop = required - (max_passengers - current_load)
            print('1')
            # if left_on_stop < 0:
            #         left_on_stop = left_on_stop * -1
            unhappy += left_on_stop
            current_load = max_passengers
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

       
 
 
    # print(f"Available capacity {available_seats}")
    
    

    
 






print(f"Unhappy customers (Total) = {unhappy}")
print(f"Total of all passengers for route = {total_passengers}")
if unhappy == 0:
    print("Customer satisfaction 100% guaranteed")
else:
    print(f"Ratio of happy to unhappy passengers{(total_passengers / unhappy) * 100}")
print("Thankyou for travelling with us today!!")

        


            
    
    


