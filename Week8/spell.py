import sys  # Import the sys module to handle command-line arguments

def load_dictionary(dict_file):
    """
    Load the dictionary file and return a set of valid words.
    
    Parameters:
    dict_file (str): The path to the dictionary file.
    
    Returns:
    set: A set of valid words.
    """
    try:
        with open(dict_file, 'r') as file:
            # Read all words and strip whitespace, converting to lowercase
            valid_words = {line.strip().lower() for line in file}
        return valid_words
    except FileNotFoundError:
        print(f"Error: The dictionary file '{dict_file}' does not exist.")
        sys.exit(1)

def spell_check(file_name, valid_words):
    """
    Check the words in the specified file against the valid words.
    
    Parameters:
    file_name (str): The name of the file to check.
    valid_words (set): A set of valid words to compare against.
    """
    try:
        with open(file_name, 'r') as file:
            # Initialize a set to hold misspelled words
            misspelled_words = set()
            
            # Read each line in the file
            for line in file:
                # Split the line into words, removing punctuation and converting to lowercase
                words = line.strip().lower().split()
                for word in words:
                    # Remove punctuation from the word
                    clean_word = ''.join(char for char in word if char.isalpha())
                    # Check if the cleaned word is not in the valid words set
                    if clean_word and clean_word not in valid_words:
                        misspelled_words.add(clean_word)
            
            # Print the misspelled words
            if misspelled_words:
                print("Misspelled words:")
                for word in sorted(misspelled_words):
                    print(word)
            else:
                print("No misspelled words found.")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        # Print usage instructions if the argument count is incorrect
        print("Usage: python spell.py <dictionary_file> <text_file>")
    else:
        # Load the dictionary and perform spell check
        dictionary_file = sys.argv[1]
        text_file = sys.argv[2]
        valid_words = load_dictionary(dictionary_file)
        spell_check(text_file, valid_words)