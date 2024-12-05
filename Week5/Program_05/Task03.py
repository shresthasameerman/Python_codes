import sys

def main():
    # Get the command-line arguments (excluding the program name)
    arguments = sys.argv[1:]

    # Check if there are any arguments provided
    if not arguments:
        print("No arguments provided.")
        return

    # Sort the arguments by their length
    shortest_argument = min(arguments, key=len)

    # Print the shortest argument
    print(f"The shortest argument is: '{shortest_argument}'")

if __name__ == "__main__":
    main()