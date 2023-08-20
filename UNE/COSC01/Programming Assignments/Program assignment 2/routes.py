import re
from operator import itemgetter

file_name = "routes.txt"
data_list = []




def read_route_data():
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):
            values = line.strip().split(',')
            if not re.match(r'^\d+(?:,\d+){2}$', line):

                
                print(f"Error in line {line_number}: Incorrect format")
                break

            try:
                route = int(values[0])
            except ValueError:
                print("Input file must only contain numbers separated by comma's.")
                break

            try:
                if route not in [routes["route"] for routes in data_list]:
                    n_happy = int(values[1])
                    n_unhappy = int(values[2])
                    if n_unhappy < 1:
                        happy_ratio = 0
                    else:

                        happy_ratio = float(format(n_happy/n_unhappy, ".2f"))
                    
                    dictionary = {
                        "route": int(values[0]),
                        "n_happy": int(values[1]),
                        "n_unhappy": int(values[2]),
                        "happy_ratio": happy_ratio
                    }
                    data_list.append(dictionary)
                else:
                    print(f"Duplicate route number in line number {line_number} of the {file_name} input file." + "\n" + f"Please verify {file_name} file contains no duplicated data and try again")
                    break
            except IndexError:
                print("Please confirm each text file row contains values separated by comma's, no spaces, for the following" + "\n" + "- Route Number" +"\n"+ "- Number Happy" +"\n" + "- Number Unhappy" )

                break
        
        

def sort_route_data():
    try:
        
        sorted_list = sorted(data_list, key=itemgetter("happy_ratio"), reverse = True)
        return sorted_list
    except ValueError:
        print()




read_route_data()
sorted_data_list = sort_route_data()






print(sorted_data_list)

# def sort_route_data():

# except (ValueError, ZeroDivisionError):