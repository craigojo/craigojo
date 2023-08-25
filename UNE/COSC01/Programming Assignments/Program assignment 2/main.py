#!/usr/bin/env python3
'''Main program file'''


# Functions required for the program are imported
from operator import itemgetter


# Resources imported from data_file_read file.
from data import read_route_data
from data import data_list


# Sets variables
extra_buses = 0


# Retrieves data_list from the read_dat_file function and sorts using the the "happy_ratio". Sorts in ascending order
# using the itemgetter function. Unexpected (unlikely) errors are handled here. 
# Data purity is ensured within the read_data_function in file (routes.py).
def sort_route_data(): 
    try:
        sorted_list = sorted(data_list, key=itemgetter("happy_ratio"), reverse = True)
        return sorted_list
    except ValueError:
        print("An un-expected error occured")


# Inputer is asked to enter number of extra busses that are available. 
# Maximum number of busses cannot exceed number of routes.
# Error are handled. Inputer is asked to enter a valid integer.
def extra_bus_routes():
    while True:
        try:

# Inputer is prmopted to enter how many routes can have an extra bus (n)
            n = int(input("How many routes can have an extra bus? "))
            list_length = len(sorted_data_list)

# Input values are validated. n cannot be greater than the number of routes.            
            if (n > 0) and n <= len(sorted_data_list):

# Extra buses are allocated to routes, allocation of buses to routes is based on happy_ratio, least happy to happy.  
                print('You should add busses for the following routes:')
                for bus in range(n):
                        extra_bus_route = sorted_data_list[bus]
                        print(f"    " + f'{extra_bus_route["route"]}')
                break

# Values less than or equal to zero are rejected
            elif n <= 0:
                 print("Enter an integer with value greater than 0")

# Values greater than number of routes are rejected. 
# User is prompted to enter a value equal to or less than number of routes
            else:
                 print(f"The value you entered {n}," + "\n" + "is greater than the number of available routes." + "\n" + f"Enter a value no greater than {list_length}" + "\n" + f"{n - (len(sorted_data_list))} busses are free for other routes" + "\n")
                 print(len(sorted_data_list))
                 
# Non integer values are handles. User is prompted to enter an integer  
        except (ValueError):
                print("Please enter a value greater than 0, no letters or characters.")

# Data read function is called, sorted data is stored in a variable (data_list()).
# The extra bus function is then called
read_route_data()
sorted_data_list = sort_route_data()
extra_bus_routes()

