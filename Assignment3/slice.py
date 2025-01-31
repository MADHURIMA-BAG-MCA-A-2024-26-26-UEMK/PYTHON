# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

# Function to slice out a specific phrase from a sentence
def slice_phrase(sentence, phrase):
    # Find the start position of the phrase
    start_position = sentence.find(phrase)
    
    if start_position != -1:
        # Slice the phrase out from the sentence
        sliced_phrase = sentence[start_position:start_position + len(phrase)]
        return sliced_phrase
    else:
        return "Phrase not found."

# Given sentence
sentence = "You cannot end a sentence with because because because is a conjunction"

# Phrase to slice out
phrase_to_slice = "because because because"

# Slice out the phrase
sliced_phrase = slice_phrase(sentence, phrase_to_slice)

# Output the sliced phrase
print(f"The sliced phrase is: '{sliced_phrase}'")
