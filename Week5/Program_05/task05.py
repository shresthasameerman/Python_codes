import sys

def main():
    # Check if any command-line arguments are provided
    if len(sys.argv) < 2:
        print("No temperature readings provided. Please provide temperature values as command-line arguments.")
        return

    # Convert command-line arguments to a list of floats
    try:
        temperatures = [float(arg) for arg in sys.argv[1:]]
    except ValueError:
        print("Please provide valid numeric temperature readings.")
        return

    # Calculate maximum, minimum, and mean
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)

    # Display the results
    print(f"Maximum Temperature: {max_temp}")
    print(f"Minimum Temperature: {min_temp}")
    print(f"Mean Temperature: {mean_temp:.2f}")

if __name__ == "__main__":
    main()