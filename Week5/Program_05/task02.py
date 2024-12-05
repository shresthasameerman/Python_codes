import sys

def main():
    # Count the number of arguments (excluding the program name)
    num_arguments = len(sys.argv) - 1
    
    # Print the number of arguments
    print(f"Number of arguments provided: {num_arguments}")

if __name__ == "__main__":
    main()