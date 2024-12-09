def find_factors(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    
    return factors

# Example usage and testing:
print(find_factors(10))  # Output: [1, 2, 5, 10]
print(find_factors(15))  # Output: [1, 3, 5, 15]
print(find_factors(28))  # Output: [1, 2, 4, 7, 14, 28]