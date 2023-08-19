import re

file_name = "routes.txt"
data_list = []

def read_route_data():
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):
            values = line.strip().split(',')
            
            if not re.match(r'^\d+(?:,\d+){2}$', line):
                print(f"Error in line {line_number}: Incorrect format")
                continue

            route=int(values[0])
            if any (routes["route"] != route for routes in data_list):
                print("Duplicate route. Please verify routes.txt file contains no duplicated data and try again")

                dictionary = {
                    "route": int(values[0]),
                    "n_happy": int(values[1]),
                    "n_unhappy": int(values[2])
                }
                data_list.append(dictionary)
            else:
                break
    





            

read_route_data()


for data in data_list:
    print(data)
