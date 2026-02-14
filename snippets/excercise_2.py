def word_frequency(text):
    words = text.split()
    dictionary = {}
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary
    
text = "ml is fun and ml is powerful"
print(word_frequency(text))
