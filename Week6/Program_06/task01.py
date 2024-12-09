def int_to_binary(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    binary_representation = ""
    
    while n > 0:
        remainder = n % 2
        binary_representation = str(remainder) + binary_representation
        n = n // 2
    
    return binary_representation

# Example usage:
print(int_to_binary(10))  # Output: '1010'
