import sys  # Import the sys module to handle command-line arguments

def wc(file_name):
    """
    Function to count the number of lines and characters in a file.
    
    Parameters:
    file_name (str): The name of the file to analyze.
    """
    try:
        # Initialize counters for lines and characters
        line_count = 0
        char_count = 0
        
        # Open the specified file in read mode
        with open(file_name, 'r') as file:
            # Iterate through each line in the file
            for line in file:
                line_count += 1  # Increment line count
                char_count += len(line)  # Increment character count by the length of the line
        
        # Print the results
        print(f"Lines: {line_count}, Characters: {char_count}")
    
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
        print("Usage: python wc.py <filename>")
    else:
        # Call the wc function with the provided filename
        wc(sys.argv[1])