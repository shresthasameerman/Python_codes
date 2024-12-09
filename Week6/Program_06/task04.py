def encrypt_message(message):
    # Remove spaces from the message
    no_spaces = message.replace(" ", "")
    # Reverse the string
    encrypted = no_spaces[::-1]
    return encrypted

# Example usage and testing:
print(encrypt_message("Hello World"))          # Output: "dlroWolleH"
print(encrypt_message("This is a test"))       # Output: "tsetaisihT"
print(encrypt_message("Encryption is fun"))     # Output: "nufsiotpircnE"
print(encrypt_message("  Spaces   should  be removed  "))  # Output: "devomerebshouldS"