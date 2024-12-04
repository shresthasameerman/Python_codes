def is_valid_integer(num):
    """Check if the integer is in the range 0 to 100 (inclusive)."""
    return 0 <= num <= 100

# Test the function
def test_is_valid_integer():
    test_cases = [-10, 0, 50, 100, 101, 200]
    for case in test_cases:
        result = is_valid_integer(case)
        print(f"is_valid_integer({case}) = {result}")

# Run the test
test_is_valid_integer()