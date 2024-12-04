def count_case_letters(s):
    """Count the number of uppercase and lowercase letters in the string."""
    uppercase_count = 0
    lowercase_count = 0
    
    for char in s:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
            
    return uppercase_count, lowercase_count

# Test the function
def test_count_case_letters():
    test_strings = [
        "Hello World!",
        "Python Programming",
        "12345",
        "Mixed CASE Letters",
        "all lowercase",
        "ALL UPPERCASE",
        "",
        "123abcDEF"
    ]
    
    for test_str in test_strings:
        upper_count, lower_count = count_case_letters(test_str)
        print(f"'{test_str}' -> Uppercase: {upper_count}, Lowercase: {lower_count}")

# Run the test
test_count_case_letters()