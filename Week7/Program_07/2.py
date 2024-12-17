def letters_in_either(word1, word2):
    return sorted(set(word1) | set(word2))  # Union of sets

def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))  # Intersection of sets

def letters_in_one_but_not_both(word1, word2):
    return sorted(set(word1) ^ set(word2))  # Symmetric difference of sets

# Testing the functions
def test_functions():
    word1 = "apple"
    word2 = "plane"

    print("Letters in at least one of the words:", letters_in_either(word1, word2))
    print("Letters in both words:", letters_in_both(word1, word2))
    print("Letters in either but not both:", letters_in_one_but_not_both(word1, word2))

# Run the test
test_functions()
