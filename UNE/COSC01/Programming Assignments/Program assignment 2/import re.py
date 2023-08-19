import re

def validate_file_format(file_path):
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            # Remove leading/trailing whitespace
            line = line.strip()
            print(line_number)

            # Check if the line matches the expected format using a regular expression
            if not re.match(r'^\d+(?:\s*,\s*\d+){3}$', line):
                print(f"Error in line {line_number}: Incorrect format")
                return False

    return True

file_path = 'routes.txt'

if validate_file_format(file_path):
    print("File format is correct.")
else:
    print("File format is incorrect.")
