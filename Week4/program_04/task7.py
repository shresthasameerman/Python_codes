def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def main():
    temperatures = []
    
    # Read 6 temperatures
    for i in range(6):
        input_temp = input(f"Enter temperature {i + 1} in Celsius (e.g., 25C): ")
        
        # Check if the input is valid
        if input_temp[-1].upper() == 'C' and input_temp[:-1].replace('.', '', 1).isdigit():
            # Extract the numeric part and convert to float
            celsius_value = float(input_temp[:-1])
            temperatures.append(celsius_value)
        else:
            print("Invalid input. Please enter a number followed by 'C'.")
            return  # Exit the program if input is invalid

    # Calculate max, min, and mean
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)

    # Display results
    print(f"Maximum temperature: {max_temp:.2f}C")
    print(f"Minimum temperature: {min_temp:.2f}C")
    print(f"Mean temperature: {mean_temp:.2f}C")

# Run the program
main()