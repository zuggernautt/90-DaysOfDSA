def can_form_word(word1, word2):
    # Convert both words to lowercase for case-insensitive comparison
    word1 = word1.lower()
    word2 = word2.lower()

    # Create a dictionary to store the count of each character in word1
    char_count = {}
    for char in word1:
        char_count[char] = char_count.get(char, 0) + 1

    # Check if each character in word2 can be found in char_count and has a non-zero count
    for char in word2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    return True