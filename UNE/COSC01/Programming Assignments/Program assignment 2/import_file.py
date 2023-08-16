# Open the file for reading
file_path = "routes.txt"

try:
    with open(file_path, 'r') as file:
        file_content = file.read()
        print("File content:")
        print(file_content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print("An error occurred:", e)