#!/usr/bin/env python3

# Exercism.io RnaTranscription - Given a DNA strand, return its RNA complement.
# Mark Lotspaih


def to_rna(dna):
    '''Given a DNA strand, return its RNA complement'''
    dnaList = list(dna)
    for i, nucleotide in enumerate(dnaList):
        if nucleotide == 'G':
            dnaList.pop(i)
            dnaList.insert(i, 'C')
        elif nucleotide == 'C':
            dnaList.pop(i)
            dnaList.insert(i, 'G')
        elif nucleotide == 'T':
            dnaList.pop(i)
            dnaList.insert(i, 'A')
        elif nucleotide == 'A':
            dnaList.pop(i)
            dnaList.insert(i, 'U')
        else:
            return ''
    return ''.join(dnaList)
