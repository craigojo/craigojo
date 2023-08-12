#!/usr/bin/env python3
max_passengers = 35             # Maximum bas seating capacity.
unhappy = 0                     # Number of passengers left behind at a stop. No room.
total_passengers=0              # Total number of passengers for route.
current_load = 0                # Current load of passegers on the bus.
stop = 0                        # Counter stores the curent stop number.
available_seats = 0             # Available seats on the bus.
number_of_stops = 0
ratio = 0                       # Ratio unhappy passengers.
first_stop = 0




# Input qestion for bus route number.
# The input is validated as an integer. Letters / words not accepted.

while True:        
    try:
        route_number = input("Please enter a route number: ")
        route_number = int(route_number)
        if route_number <= 0:
            print("Invalid route number, Please enter a positive integer")
        else:
            break
    except ValueError:
        print("Invalid route number, Please enter a positive integer")
print(f"Route Number = {route_number}")




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
        print("Invalid number of stops, enter an integer with value greater than 2")
last_stop = number_of_stops - 1
print(f"Number of stops on this route = {number_of_stops}")




# Starts bus stop loop.
# Question, How many to depart at stop. Stop number is retrieved from stop variable,
# incremented by 1 and displayed to the console.

while stop < number_of_stops:    
    if stop != first_stop:
        while True:
            passengers_off =  input(f"How many passengers left the bus at stop #{stop + 1}?  ")
            try:
                passengers_off = int(passengers_off)
                if passengers_off < 0:
                    print("Invalid number of passengers, Please enter a positve integer")
                elif (passengers_off > current_load) and (stop != last_stop):
                    print(f"Invalid number of passengers. Only {current_load} passengers were on the bus.")
                elif stop == last_stop and current_load != passengers_off:
                    print(f"This is the last stop. There should be {current_load} passengers leaving.")
                else:
                    current_load -= passengers_off
                    break
            except ValueError:
                print("Invalid number of passengers, Please enter a positve integerr")

        print(f"Passengers departed bus stop at {stop + 1} = {passengers_off} ")
 



# Question, How many waiting at stop. Stop number is retrieved from stop variable,
# incremented by 1 and displayed to the console.

    if stop != last_stop:
        while True:
            current_stop_unhappy = 0
            passengers_on = input(f"How many passengers were waiting to get on at stop #{stop + 1}?  ")
            try:
                passengers_on = int(passengers_on)
                if passengers_on < 0:
                    print("Invalid number of passengers, Please enter a positve integer")
                    continue
                elif (current_load + passengers_on) > max_passengers:
                    current_stop_unhappy = current_load + passengers_on - max_passengers
                    unhappy += current_stop_unhappy
                    print(f"Available seats {max_passengers - current_load}, {current_stop_unhappy} waited for the next bus")
                current_load += passengers_on - current_stop_unhappy
                total_passengers += passengers_on - current_stop_unhappy
                break
            except ValueError:
                print("Please enter a number")
        print(f"Passengers boarding bus stop at {stop + 1} = {passengers_on - current_stop_unhappy} ")   
    stop += 1




# The following print statements contain values for.
#   - Total for all passengers that boarded the bus.
#   - Total for passengers left waiting along the route.
#   - Ratio of unhappy passengers to happy passengers to two decimal places.
  
print(f"Route number: {route_number}")
print(f"Happy customers: {total_passengers}")
print(f"Unhappy customers: {unhappy}")
try:
    ratio = float(format(total_passengers/unhappy, ".2f"))
    print(f"Ratio of happy to unhappy passengers: {ratio}")
except ZeroDivisionError:
    print(f"Ratio of happy to unhappy passengers: 0.00")

