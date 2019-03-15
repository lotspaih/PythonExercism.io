#! /usr/bin/env python3

# Exercism.io Run Length Encoding - Implement run-length encoding and decoding.
# Mark Lotspaih


def encode(textInput):
    '''Implements run-length encoding'''
    listTextInput = list(textInput)
    listTextInput.append('  ')
    encodedOutput = []
    count = 0
    previous = listTextInput[0]
    for i in range(len(listTextInput)):
        if listTextInput[i] == previous:
            count += 1
        else:
            if count > 1:
                encodedOutput.append(str(count) + listTextInput[i - 1])
            else:
                encodedOutput.append(listTextInput[i - 1])
            previous = listTextInput[i]
            count = 1
    return ''.join(encodedOutput)


def decode(encodedInput):
    '''Implements run-length decoding'''
    import re
    decodeRegex = re.compile('((\\d*)(\\D?))(\\D*)')
    textOutput = []
    for item in decodeRegex.finditer(encodedInput):
        if item.group(1).isalpha():
            textOutput.append(item.group(1))
        if item.group(2):
            textOutput.append(item.group(3) * int(item.group(2)))
        if item.group(4):
            textOutput.append(item.group(4))
    return ''.join(textOutput)
