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
    try:
        route_number = input("What is the route number: ")
        route_number = int(route_number)
        if route_number <= 0:
            print("Invalid route number, Please enter a positive integer")
        else:
            break
    except ValueError:
        print("Please enter a number")
print(f"Bus Route Number = {route_number}")


# Question for number of stops along bus route
# The input is validated as an integer. letters / words not accepted.

while True:
    try:
        number_of_stops = input("Please enter the number of stops on this route: " )
        number_of_stops = int(number_of_stops)
        if  number_of_stops < 3:
            print("Invalid number of stops, enter an integer with value greater than 2")
        else:
            break
    except ValueError:
        print("Please enter a number")
print(f"Number of stops on this route = {number_of_stops}")


first_stop = 0
last_stop = number_of_stops - 1
# Starts bus stop loop.
# Question, How many waiting at stop. Stop number is retrieved from stop variable,
# incremented by 1 and displayed to the console.
while stop < number_of_stops:

    # Question, How many to depart at stop. Stop number is retrieved from stop variable,
# incremented by 1 and displayed to the console.

    
    if stop != first_stop:
        while True:
            get_off =  input(f"How many to depart at bus stop {stop + 1}?")
            try:
                get_off = int(get_off)
                if get_off < 0:
                    print("Invalid number of passengers, Please enter a non-negative integer")
                elif get_off > current_load:
                    print(f"Departing passengers cannot be larger than current passengers ({current_load}) in the bus. Please try again.")
                elif stop == last_stop and current_load != get_off:
                    print(f"Invalid number of passengers. Only {current_load} passengers were on the bus")
                else:
                    current_load -= get_off
                    break
            except ValueError:
                print("Please enter a number")

        print(f"Passengers waiting to depart bus at stop {stop + 1} = {get_off}")
   

    if stop != last_stop:
        while True:
            current_stop_unhappy = 0
            get_on = input(f"How many passengers were waiting to get on at stop {stop + 1}?")
            try:
                get_on = int(get_on)
                if get_on < 0:
                    print("Invalid number of passengers, Please enter a non-negative integer")
                    continue
                elif (current_load + get_on) > max_passengers:
                    current_stop_unhappy = current_load + get_on - max_passengers
                    unhappy += current_stop_unhappy
                    print(f"Sorry, our maximum capacity is 35, {current_stop_unhappy} will need to wait for the next bus")
                current_load += get_on - current_stop_unhappy
                total_passengers += get_on - current_stop_unhappy
                break
            except ValueError:
                print("Please enter a number")

   # print(f"Passengers waiting at bus stop {stop + 1} = {get_on}")


 # Calculates bus seat availablity. Calculation is derived from passengers waiting / departing.   
   
    stop += 1
  
    

    
 






print(f"Unhappy customers (Total) = {unhappy}")
print(f"Total of all passengers for route = {total_passengers}")
if unhappy == 0:
    print("Customer satisfaction 100% guaranteed")
else:
    print(f"Ratio of happy to unhappy passengers {(total_passengers / unhappy)}")
print("Thankyou for travelling with us today!!")

        


            
    
    


