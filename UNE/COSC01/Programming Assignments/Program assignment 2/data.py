# Functions required for the program are imported (regex)
import re

# File containing raw route data is refrenced here. Is allocated a variable.
file_name = "routes.txt"

# Stores filtered data retrieved from the raw data file, that has passed the read_route_data function.
data_list = []


def read_route_data():
# Clears the storage file from previous entries.
    data_list.clear()               
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):
# Iterates through the text file
# Spaces are removed, contents indentified by commas.            
            values = line.strip().split(',')

# File is read line by line,
# regex is used to capture 3 groups of integers per line                            
            if not re.match(r'^\d+(?:,\d+){2}$', line):

 # Integers only, in groupings of 3                
                print(f"Error in line {line_number}: Incorrect format")     
                break
            try:
                route = int(values[0])

# Captures invalid entries, accepts integers only.
            except ValueError:                                                              
                print("Input file must only contain numbers separated by comma's.")     
                break


            try:
# Eliminates potential for DivideByZero error.                                                                            
                if route not in [routes["route"] for routes in data_list]:                  
                    n_happy = int(values[1])                                                
                    n_unhappy = int(values[2])
                    if n_unhappy < 1:
                        happy_ratio = 0

# Calculates happy_ratio 
                    else:                                                                                           
                        happy_ratio = float(format(n_happy/n_unhappy, ".2f"))

# Associates key with a value.                   
                    dictionary = {                                                          
                        "route": int(values[0]),
                        "n_happy": int(values[1]),
                        "n_unhappy": int(values[2]),
                        "happy_ratio": happy_ratio
                    }
# Stores values into a new dictionary within list, data_list.
                    data_list.append(dictionary)
# Captures duplicates within data. Prompts user to check file. Program exits                                          
                else:
                    print(f"Duplicate route number in line number {line_number} of the {file_name} input file." + "\n" + f"Please verify {file_name} file contains no duplicated data and try again")
                    break
# Captures exceptions. IndexError. Prompts user to verify raw file contains integers in groups of 3 per line, separated by commas only, no spaces.
            except IndexError:
                print("Please confirm each text file row contains values separated by comma's, no spaces, for the following" + "\n" + "- Route Number" +"\n"+ "- Number Happy" +"\n" + "- Number Unhappy" )

                break

