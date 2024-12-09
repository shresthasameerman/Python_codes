import random
import string

def encrypt_with_random_letters(message):
    # Generate a random interval between 2 and 20
    interval = random.randint(2, 20)
    
    # Initialize the encrypted message
    encrypted_message = []
    
    # Iterate through the message and insert random letters
    for i in range(len(message)):
        # Append the current character of the message
        encrypted_message.append(message[i])
        
        # Insert a random letter after every 'interval' characters
        if (i + 1) % interval == 0 and (i + 1) != len(message):  # Check if we are at the interval
            random_letter = random.choice(string.ascii_lowercase)  # Choose a random letter
            encrypted_message.append(random_letter)  # Append the random letter
    
    # Join the list into a string
    encrypted_message_str = ''.join(encrypted_message)
    
    return encrypted_message_str, interval

# Example usage and testing
message = "send cheese"
encrypted_message, interval = encrypt_with_random_letters(message)
print(f"Original message: '{message}'")
print(f"Random interval: {interval}")
print(f"Encrypted message: '{encrypted_message}'")