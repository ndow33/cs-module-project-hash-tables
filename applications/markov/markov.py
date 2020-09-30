import random
import os

# Read in all the words in one go
with open("applications\markov\input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
words = words.split()
# create a dictionary to house the words
d = {}
# loop through all the words in words
counter = 0
for word in words:
    # if the word is not in the dictionary
    if word not in d:
        # create a list to be held in the dictionary
        l = []
        # add the word to the dictionary
        # with an empty list as the value
        d[word] = l
    # once the word is in the dictionary
    # get the next word
    next_word = words[counter + 1]
    # put that word in the list
    d[word].append(next_word)
    # increment counter
    if counter < len(words)-2:
        counter += 1   


# TODO: construct 5 random sentences of 10 words each
for x in range(0,5):
    # create an empty string
    s = ''
    # get a random word
    rando = words[random.randint(0, len(words)-1)]
    s = s + rando
    for x in range(0,10):
        # retrieve that random word's possible values from the dictionary
        next_word = d[rando][random.randint(0, len(d[rando])-1)]
        s = s + ' ' + next_word
        rando = next_word
    
    print(s)