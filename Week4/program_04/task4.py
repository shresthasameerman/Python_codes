def remove_last_character(input_string):
    # Check if the string has one or fewer characters
    if len(input_string) <= 1:
        return input_string
    else:
        # Return the string without the last character
        return input_string[:-1]

# Test the function with various inputs
print(remove_last_character("Hello"))  # Output: "Hell"
print(remove_last_character("Python"))  # Output: "Pytho"
print(remove_last_character("A"))       # Output: "A"
print(remove_last_character(""))         # Output: ""
print(remove_last_character("Test\n"))   # Output: "Test"