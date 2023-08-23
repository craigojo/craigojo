# Functions required for the program are imported
import re

# File containing bus data is refrenced here. The storage file is created.
file_name = "routes.txt"
data_list = []


def read_route_data():
    data_list.clear()               # Clears the storage file from previous entries
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):                 # Enumerate loops through the text file
            values = line.strip().split(',')                                # File is read line by line, Spaces are removed, contents indentified by commas.
            if not re.match(r'^\d+(?:,\d+){2}$', line):                     # regex is used to capture 3 groups of integers per line

                
                print(f"Error in line {line_number}: Incorrect format")     # Integers only, in groupings of 3 
                break

            try:
                route = int(values[0])
            except ValueError:                                                              # Captures invalid entries, accepts integers only.
                print("Input file must only contain numbers separated by comma's.")     
                break

            try:                                                                            
                if route not in [routes["route"] for routes in data_list]:                  # Eliminates potential for DivideByZero error,
                    n_happy = int(values[1])                                                
                    n_unhappy = int(values[2])
                    if n_unhappy < 1:
                        happy_ratio = 0
                    else:
                                                                                            
                        happy_ratio = float(format(n_happy/n_unhappy, ".2f"))               # Calculates happy_ratio
                    
                    dictionary = {                                                          # Stores values into a dictionary
                        "route": int(values[0]),
                        "n_happy": int(values[1]),
                        "n_unhappy": int(values[2]),
                        "happy_ratio": happy_ratio
                    }
                    data_list.append(dictionary)                                            # Dictionary is added to the data_list store.
                else:
                    print(f"Duplicate route number in line number {line_number} of the {file_name} input file." + "\n" + f"Please verify {file_name} file contains no duplicated data and try again")
                    break
            except IndexError:
                print("Please confirm each text file row contains values separated by comma's, no spaces, for the following" + "\n" + "- Route Number" +"\n"+ "- Number Happy" +"\n" + "- Number Unhappy" )

                break

