#Takes an encrypted message from a file and decrpyts ot useing ceasar's cipher. then it puts the information into a new file that it creates.

import os # Import the os module for path operations
print("Current working directory:", os.getcwd())
# Prompt the user for the file path
inputFilename = input("Enter the input file: ").strip()
outputFilename = input("Enter the output file: ").strip()
increment_by = input("What is your key? ")


def increase_ascii_value(content, increment_value): #gets ascii value and makes a new string
    new_characters = []
    for char in content:
        if ord(char) > 32:
            new_char_code = ord(char) - int(increment_value)
        elif ord(char) < 32:
            new_char_code = ord(char)
        try:
            new_char = chr(new_char_code)
            new_characters.append(new_char)
        except ValueError:
            # Handle cases where the new value is outside the valid Unicode range
            print(f"Warning: ASCII value {new_char_code} is out of range for character '{char}'. Skipping or handling differently.")

    return "".join(new_characters)

try: # Opens file and reads it
    # Open the file in read mode ('r') using a context manager
    with open(inputFilename, 'r') as file:
        # Read the contents of the file
        content = file.read()
        print("File opened successfully. Program finished")
        modified_string = increase_ascii_value(content, increment_by) 
        with open(outputFilename, "a") as f:
            f.write(modified_string)
        # print("Absolute path:", os.path.abspath(filename))
        # print("File size:", os.path.getsize(filename))

except FileNotFoundError: #if there is error
    print(f"Error: The file '{inputFilename}' was not found.")
except IOError as e:
    # Handles other potential I/O errors (e.g., permissions)
    print(f"Error: An I/O error occurred - {e}")

