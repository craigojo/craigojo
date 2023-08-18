# Read the text file and split it into lines
with open("routes.txt", "r") as file:
    lines = file.readlines()

# Initialize an empty list to store dictionaries
data_list = []

# Iterate through each line in the file
for line in lines:
    
    # Split the line into individual values
    values = line.strip().split(',')


# Create a dictionary with keys and values
    dictionary = {
        "Route": int(values[0]),
        "n_happy": int(values[1]),
        "n_unhappy": int(values[2])
    }
    if dictionary not in data_list:
# Append the dictionary to the list
        data_list.append(dictionary)

# Print the list of dictionaries
for data in data_list:
    print(data)
