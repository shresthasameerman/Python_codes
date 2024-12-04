def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

# Test the functions
# Testing Celsius to Fahrenheit
celsius_temp = 25
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp:.2f}°F")

# Testing Fahrenheit to Celsius
fahrenheit_temp = 77
celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp}°F is equal to {celsius_temp:.2f}°C")

# Additional tests
print(f"0°C is equal to {celsius_to_fahrenheit(0):.2f}°F")  # Should be 32°F
print(f"100°C is equal to {celsius_to_fahrenheit(100):.2f}°F")  # Should be 212°F
print(f"32°F is equal to {fahrenheit_to_celsius(32):.2f}°C")  # Should be 0°C
print(f"212°F is equal to {fahrenheit_to_celsius(212):.2f}°C")  # Should be 100°C