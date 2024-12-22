import sys  # Import the sys module to handle command-line arguments

def nl(file_name):
    """
    Function to print the contents of a file with line numbers.
    
    Parameters:
    file_name (str): The name of the file to read.
    """
    try:
        # Open the specified file in read mode
        with open(file_name, 'r') as file:
            # Enumerate through each line in the file, starting line numbers at 1
            for line_number, line in enumerate(file, start=1):
                # Print the line number followed by the line content
                print(f"{line_number}\t{line}", end='')  # Use end='' to avoid double newlines
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        # Print usage instructions if the argument count is incorrect
        print("Usage: python nl.py <filename>")
    else:
        # Call the nl function with the provided filename
        nl(sys.argv[1])