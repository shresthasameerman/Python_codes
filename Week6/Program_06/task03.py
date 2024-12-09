def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if n <= 3:
        return True  # 2 and 3 are prime numbers
    
    # Check for even numbers and multiples of 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check for factors from 5 to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # Check only 6k ± 1
    
    return True

# Example usage and testing:
print(is_prime(1))   # Output: False
print(is_prime(2))   # Output: True
print(is_prime(3))   # Output: True
print(is_prime(4))   # Output: False
print(is_prime(5))   # Output: True
print(is_prime(29))  # Output: True
print(is_prime(30))  # Output: False
print(is_prime(97))  # Output: True