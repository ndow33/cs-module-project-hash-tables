'''Implement functionality to reverse an input string. Print out the reversed string.

For example, given a string "cool", print out the string "looc".

You may use whatever programming language you'd like.

Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.'''


def reverse(s):
    '''    # find the length
    index = len(s) - 1
    # create a new string
    new_string = ''
    # loop through each index until we reach 0
    while index >= 0:
        new_string = new_string + s[index]
        index -= 1
    # return the new string
    return new_string  
    '''
    return s[::-1]  


test = 'test'
print(reverse(test))
    
