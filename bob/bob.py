#! /usr/bin/env python3

# Exercism.io Bob - Bob is a lackadaisical teenager. In conversation,
#    his responses are very limited.
# Mark Lotspaih


def hey(userInput):
    '''Bob is a lackadaisical teenager. In conversation,
    his responses are very limited.'''
    import string
    userInputAll = userInput.rstrip()
    for char in userInput:
        if char in string.punctuation:
            userInput = userInput.replace(char, '')
    userInput = userInput.strip()
    if userInput.isupper():
        return 'Whoa, chill out!'
    elif userInputAll.endswith('?'):
        return 'Sure.'
    elif not userInput:
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
