def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def main():
    # Get input from the user
    input_temp = input("Enter temperature in Celsius (e.g., 25C): ")
    
    # Check if the input is valid
    if input_temp[-1].upper() == 'C' and input_temp[:-1].replace('.', '', 1).isdigit():
        # Extract the numeric part and convert to float
        celsius_value = float(input_temp[:-1])
        
        # Convert to Fahrenheit
        fahrenheit_value = celsius_to_fahrenheit(celsius_value)
        
        # Display the result in the same format
        print(f"{fahrenheit_value:.2f}F")
    else:
        print("Invalid input. Please enter a number followed by 'C'.")

# Run the program
main()