#!/usr/bin/env python3

# Exercism.io Word Count - Given a phrase, count the occurrences of each word
#    in that phrase.
# Mark Lotspaih


def word_count(phrase):
    '''Given a phrase, count the occurrences of each word in that phrase.'''
    import string
    for char in phrase:
        if char in string.punctuation:
            phrase = phrase.replace(char, ' ')
    phraseLower = phrase.lower()
    phraseList = list(phraseLower.split())
    phraseDict = {}
    for word in phraseList:
        listCount = phraseList.count(word)
        phraseDict[word] = listCount
    return phraseDict
