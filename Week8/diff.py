import sys  # Import the sys module to handle command-line arguments

def compare_files(file1, file2):
    """
    Function to compare the contents of two files.
    
    Parameters:
    file1 (str): The name of the first file to compare.
    file2 (str): The name of the second file to compare.
    """
    try:
        # Open both files in read mode
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            # Read the contents of both files
            content1 = f1.read()
            content2 = f2.read()
            
            # Compare the contents of the two files
            if content1 == content2:
                print("The files are the same.")
            else:
                print("The files are different.")
    
    except FileNotFoundError as e:
        # Handle the case where one or both files do not exist
        print(f"Error: {e}")
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        # Print usage instructions if the argument count is incorrect
        print("Usage: python diff.py <file1> <file2>")
    else:
        # Call the compare_files function with the provided filenames
        compare_files(sys.argv[1], sys.argv[2])