max_passengers = 35                         # Maximum bus seating capacity.
unhappy = 0                                 # Totals the number of passengers left behind for route.
total_passengers=0                          # Total number of passengers for route.
current_load = 0                            # Current load of passegers on the bus.
stop = 0                                    # Counter stores the current stop number.
number_of_stops = 0                         # Number of stops along the route.
first_stop = 0
last_stop = number_of_stops - 1




# Input qestion for bus driver to enter route number.
# The input is validated as a positive integer. Letters / words not accepted.

while True:        
    try:
        route_number = input("What is the route number: ")
        route_number = int(route_number)
        if route_number <= 0:
            print("Invalid route number, Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Please enter a number, letters or words not accepted.")
print(f"Bus Route Number = {route_number}")





# Question for number of stops along bus route.
# The input is validated as a postive integer. Letters / words not accepted.

while True:
    try:
        number_of_stops = input("Please enter the number of stops on this route: " )
        number_of_stops = int(number_of_stops)
        if  number_of_stops < 3:
            print("Invalid number of stops, enter an integer with value greater than 2.")
        else:
            break
    except ValueError:
        print("Please enter a number, letters or words not accepted.")
print(f"Number of stops on this route = {number_of_stops}")




# Starts bus stop loop.

# Question, How many waiting to depart bus at the stop. The while function verifies stop number is less than the stored variable value.
# The driver is asked how many will depart the bus. The value provided by the driver is checked and must be less than or equal to the 
# current number of passengers on the bus. If stop is last stop the driver is prompted to specify how many will depart the bus, 
# the value provided must equal current number of passengers on the bus. 
# The input is validated as a postive integer. Letters / words not accepted.

while stop < number_of_stops:    
    if stop != first_stop:
        while True:
            commuter_on =  input(f"How many to depart at bus stop {stop + 1}?")
            try:
                commuter_on = int(commuter_on)
                if commuter_on < 0:
                    print("Invalid number of passengers, Please enter a non-negative integer")
                elif commuter_on > current_load:
                    print(f"Departing passengers cannot be larger than current passengers ({current_load}) in the bus. Please try again.")
                elif stop == last_stop and current_load != commuter_on:
                    print(f"Invalid number of passengers. Only {current_load} passengers were on the bus.")
                else:
                    current_load -= commuter_on
                    break
            except ValueError:
                print("Please enter a number, letters or words not accepted.")

        print(f"Passengers waiting to depart bus at stop {stop + 1} = {commuter_on}.")




# Question, How many waiting to board bus at the stop. The while function verifies stop number is less than the stored variable value.
# The number of passengers to board the bus is compared to current passenger load subtracted from bus capacity
# The unhappy variable stores passengers left waiting at the stop.

    if stop != last_stop:
        while True:
            current_stop_unhappy = 0
            commuter_off = input(f"How many passengers were waiting to get on at stop {stop + 1}?")
            try:
                commuter_off = int(commuter_off)
                if commuter_off < 0:
                    print("Invalid number of passengers, Please enter a non-negative integer.")
                    continue
                elif (current_load + commuter_off) > max_passengers:
                    current_stop_unhappy = current_load + commuter_off - max_passengers
                    unhappy += current_stop_unhappy
                    print(f"Sorry, our maximum capacity is 35, {current_stop_unhappy} will need to wait for the next bus.")
                current_load += commuter_off - current_stop_unhappy
                total_passengers += commuter_off - current_stop_unhappy
                break
            except ValueError:
                print("Please enter a number, letters or words not accepted.")

        print(f"Passengers waiting at bus stop {stop + 1} = {commuter_off}")

    stop += 1
  
    

    
 




# The following print statements contain values for.
#   - Total for all passengers that boarded the bus.
#   - Total for passengers left waiting along the route.
#   - Ratio of unhappy passengers to happy passengers to two decimal places.

print(f"Unhappy customers (Total) = {unhappy}.")
print(f"Total of all passengers for route = {total_passengers}.")
if unhappy == 0:
    print("Customer satisfaction 100% guaranteed.")
else:

    ratio = float(format(unhappy/total_passengers, ".2f"))
    print(f"Ratio of happy to unhappy passengers {ratio}")
print("Thankyou for travelling with us today!!")



