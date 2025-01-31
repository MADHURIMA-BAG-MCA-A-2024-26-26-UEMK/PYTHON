# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

# Function to find the position of the first occurrence of the word 'because'
def find_first_occurrence(sentence, word):
    # Find the position of the first occurrence of 'because'
    position = sentence.find(word)
    return position

# Given sentence
sentence = "You cannot end a sentence with because because because is a conjunction"

# Word to search for
word_to_find = "because"

# Get the position of the first occurrence
position = find_first_occurrence(sentence, word_to_find)

# Output the position
print(f"The first occurrence of the word '{word_to_find}' is at position: {position}")
