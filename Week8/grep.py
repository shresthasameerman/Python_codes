import sys  # Import the sys module to handle command-line arguments

def grep(pattern, file_name):
    """
    Function to search for a pattern in a file and print matching lines.
    
    Parameters:
    pattern (str): The string to search for in the file.
    file_name (str): The name of the file to search.
    """
    try:
        # Open the specified file in read mode
        with open(file_name, 'r') as file:
            # Initialize a flag to check if any lines match
            found = False
            
            # Iterate through each line in the file
            for line_number, line in enumerate(file, start=1):
                # Check if the pattern is in the current line
                if pattern in line:
                    # Print the matching line with its line number
                    print(f"{line_number}: {line}", end='')  # Use end='' to avoid double newlines
                    found = True
            
            # If no lines were found, print a message
            if not found:
                print(f"No lines found containing '{pattern}' in '{file_name}'.")
    
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        # Print usage instructions if the argument count is incorrect
        print("Usage: python grep.py <pattern> <filename>")
    else:
        # Call the grep function with the provided pattern and filename
        grep(sys.argv[1], sys.argv[2])