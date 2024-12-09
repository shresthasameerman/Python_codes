import random
import string

def encrypt_with_random_letters(message):
    # Generate a random interval between 2 and 20
    interval = random.randint(2, 20)
    print(f"Random interval for encryption: {interval}")  # Debugging line
    
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
            print(f"Inserted random letter '{random_letter}' after index {i}")  # Debugging line
    
    # Join the list into a string
    encrypted_message_str = ''.join(encrypted_message)
    
    return encrypted_message_str, interval

def decrypt_message(encoded_message, interval):
    # Initialize an empty list to hold the original message characters
    original_message = []
    
    # Iterate through the encoded message
    for i in range(len(encoded_message)):
        # Check if the current index is a position of the original message
        if (i + 1) % (interval + 1) != 0:  # Skip every (interval + 1)th character
            original_message.append(encoded_message[i])
    
    # Join the list into a string to form the original message
    decrypted_message = ''.join(original_message)
    
    return decrypted_message

# Example usage
message = "send cheese"
encrypted_message, interval = encrypt_with_random_letters(message)
print(f"Original message: '{message}'")
print(f"Encrypted message: '{encrypted_message}'")

# Decrypt the message
decrypted_message = decrypt_message(encrypted_message, interval)
print(f"Decrypted message: '{decrypted_message}'")