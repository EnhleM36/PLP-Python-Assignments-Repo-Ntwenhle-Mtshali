filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        content = file.read()

    modified_content = content.upper()

    output_filename = 'modified_' + filename
    with open(output_filename, 'w') as new_file:
        new_file.write(modified_content)

    print(f"Modified content has been written to '{output_filename}'.")

except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Could not read or write to the file.")
