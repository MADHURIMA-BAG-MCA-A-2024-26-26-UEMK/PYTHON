# Create an acronym or an abbreviation for the name 'Python For Everyone'.

# Function to create an acronym from the given phrase
def create_acronym(phrase):
    words = phrase.split()  # Split the phrase into words
    acronym = ''.join(word[0].upper() for word in words)  # Take the first letter of each word and capitalize it
    return acronym

# Input the phrase
input_phrase = "Python For Everyone"

# Generate the acronym
acronym = create_acronym(input_phrase)

# Output the acronym
print(f"The acronym for '{input_phrase}' is: {acronym}")
