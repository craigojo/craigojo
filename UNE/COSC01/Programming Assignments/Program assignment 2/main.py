#!/usr/bin/env python3
# Functions required for the program are imported
from operator import itemgetter



# Resources imported from data_file_read file.
from data import read_route_data
from data import data_list



# Sets variables
extra_buses = 0



# Retrieves sorted data using the the "happy_ratio" from the read_dat_file function, sorts in ascending order
# using the itemgetter function. Unexpected errors are handled here. Data purity is ensured within the read_data_function.
def sort_route_data(): 
    try:
        sorted_list = sorted(data_list, key=itemgetter("happy_ratio"), reverse = True)
        return sorted_list
    except ValueError:
        print("An un-expected error occured")



# Inputer is asked to enter number of extra busses that are available. 
# Assumes maximum number of busses wont exceed number of routes.
# Error are handled. Inputer is asked to enter a valid integer.
def extra_bus_routes():
    while True:
        try:
            extra_buses = int(input("How many routes can have an extra bus? "))
            list_length = len(sorted_data_list)
            
            if (extra_buses > 0) and extra_buses <= len(sorted_data_list):   
                print('You should add busses for the following routes:')
                for bus in range(extra_buses):
                        extra_bus_route = sorted_data_list[bus]
                        print(f"    " + f'{extra_bus_route["route"]}')
                break
            elif extra_buses <= 0:
                 print("Enter an integer with value greater than 0")
            else:
                 print(f"The value you entered {extra_buses}," + "\n" + "is greater than the number of available routes." + "\n" + f"Enter a value no greater than {list_length}" + "\n" + f"{extra_buses - list_length} busses are free for other routes" + "\n")
                
        except (ValueError):
                print("Please enter a value greater than 0, no letters or characters.")


# Data read function is called, sorted data is stored in a variable.
# The extra bus function is then called
read_route_data()
sorted_data_list = sort_route_data()
extra_bus_routes()

