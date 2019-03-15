#!/usr/bin/env python3

# Exercism.io Isogram - Determine if a word or phrase is an isogram.
# Mark Lotspaih


def is_isogram(word):
    '''Determine if a word or phrase is an isogram and return True if it is
    and False if it is not.'''
    orig = list(word.lower())
    for letter in orig:
        if letter.isalpha():
            if orig.count(letter) > 1:
                return False
            else:
                continue
    return True
