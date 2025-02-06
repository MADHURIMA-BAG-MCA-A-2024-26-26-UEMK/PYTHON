def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    
    for word in words:
        word = word.lower()  # Make case-insensitive
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency

# Example usage
sentence = "Hello world hello Python hello"
print(word_frequency(sentence))
