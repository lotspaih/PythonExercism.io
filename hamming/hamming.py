#!/usr/bin/env python3

# Exercism.io Hamming - Calculate the Hamming difference between two DNA
#    strands.
# Mark Lotspaih


def distance(strand1, strand2):
    '''Calculates the Hamming difference between two DNA strands.'''
    listStrand1 = list(strand1)
    listStrand2 = list(strand2)
    if len(listStrand1) == len(listStrand2):
        if listStrand1 == listStrand2:
            return 0
        else:
            differences = 0
            for i, item in enumerate(listStrand1):
                if listStrand1[i] != listStrand2[i]:
                    differences += 1
                else:
                    continue
            return differences
    else:
        raise ValueError
