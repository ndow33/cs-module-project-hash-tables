def no_dups(s):
    # split s into individual words
    s = s.split()
    # create a dictionary to hold the words
    d = {}
    new_string = ''
    # loop through the words
    for word in s:
        # if the word is not in the dictionary
        if word not in d:
            # add it to the dictionary
            d[word] = word
            new_string = new_string + word + ' '

    new_string = new_string[:-1]

    return new_string
    



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))