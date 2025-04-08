#A simple file handling program that reads a file, modifies its content, and writes it to another file.
# This program reads a file, converts its content to uppercase, and writes it to another file.
file1 = "file1.txt"
file2 = "file2.txt"

# Open file1.txt in read mode and file2.txt in write mode
try:
    with open(file1, "r") as infile:
        content = infile.read() # Ensures the file is closed after reading

        modified_content = content.upper() # Convert content to uppercase


        with open(file2, "w") as outfile:
            outfile.write(modified_content)# Ensures the file is closed after writing

        # Print the modified content to the console
        print(f"Content from  file1.txt has been modified and written to file2.txt in uppercase.")

# Print the modified content to the console
        print(modified_content)

# Handle specific exceptions
except FileNotFoundError:# This exception is raised when the file is not found.
    print(f"Error: {file1} not found.")

except IOError:# This exception is raised when an I/O operation fails.
    print("An error occurred while reading or writing files.")

except PermissionError:# This exception is raised when the program does not have permission to read or write the file.
    print(f"Permission denied: Unable to read {file1} or write to {file2}.")

except Exception as e:# This is a general exception handler that catches any other exceptions that may occur.
    print(f"An unexpected error occurred: {e}")


