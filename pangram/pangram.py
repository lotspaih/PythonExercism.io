#!/usr/bin/env python3

# Exercism.io Pangram - Determine if a sentence is a pangram.
# Mark Lotspaih


def is_pangram(sentence):
    '''Determine if a sentence is a pangram and return True if it is or
    False if it is not.'''
    alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z']
    sentenceList = list(sentence.lower())
    if sentenceList:
        for letter in alphabetList:
            for character in sentenceList:
                if character.isalpha():
                    if letter not in sentenceList:
                        return False
                    else:
                        continue
        return True
    return False
