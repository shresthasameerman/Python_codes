def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def main():
    temperatures = []
    
    print("Enter temperatures in Celsius (e.g., 25C). Press Enter to finish.")
    
    while True:
        input_temp = input("Enter temperature: ")
        
        # Check if the input is empty (user pressed Enter)
        if input_temp == "":
            break
        
        # Check if the input is valid
        if input_temp[-1].upper() == 'C' and input_temp[:-1].replace('.', '', 1).isdigit():
            # Extract the numeric part and convert to float
            celsius_value = float(input_temp[:-1])
            temperatures.append(celsius_value)
        else:
            print("Invalid input. Please enter a number followed by 'C'.")

    # Check if any temperatures were entered
    if temperatures:
        # Calculate max, min, and mean
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)

        # Display results
        print(f"Maximum temperature: {max_temp:.2f}C")
        print(f"Minimum temperature: {min_temp:.2f}C")
        print(f"Mean temperature: {mean_temp:.2f}C")
    else:
        print("No valid temperatures were entered.")

# Run the program
main()