def unique_sorted_letters(input_string):
    # Use a set to get unique letters and convert to lowercase
    unique_letters = set(input_string.lower())
    # Filter out non-alphabetic characters
    unique_letters = {char for char in unique_letters if char.isalpha()}
    # Sort the unique letters and return as a list
    return sorted(unique_letters)

# Test the function
test_string = "cheese"
result = unique_sorted_letters(test_string)
print(result)  # Output should be ['c', 'e', 'h', 's']