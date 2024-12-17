def frequency_analysis(message):
    # Initialize a dictionary to count letter frequencies
    letter_counts = {}
    
    # Process each character in the message
    for char in message.lower():  # Convert to lowercase for case insensitivity
        if char.isalpha():  # Only consider letters
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    
    # Sort the dictionary items by the counts in descending order
    sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Report the six most common letters
    print("Six most common letters:")
    for letter, count in sorted_letters[:6]:
        print(f"{letter}: {count}")

# Example usage
if __name__ == "__main__":
    message = """
    Tqfdmbtrm tgfo xmbk. Fqfbsqbtm yplz cbmlbozqo eib tgfo. Ltzl tgfo cbrffbo
    tgfo yfohbo bqfxfq.
    """
    frequency_analysis(message)
