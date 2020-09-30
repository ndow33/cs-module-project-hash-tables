def word_count(s):
    # filter out the unwanted characters from the original string
    pro = ['"', ':', ';', ',', '.', '-', '+', '=', '/', "\\", '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    for letter in s:
        for char in pro:
            if letter == char:
                s = s.replace(letter, ' ')
    # make the input lowercase
    s = s.lower()
    # split the sentence into a list of words
    s = s.split()
    # create a dictionary to house the word counts
    d = {}
    for word in s:
        # loop through the prohibited values
        #for 
        # if the word is in the dictionary
        if word in d:
            # add 1 to its value
            d[word] += 1
        # if the word is not in the dictionary
        else:
            d[word] = 1
    

    return d



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('a a\ra\na\ta \t\r\n'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))