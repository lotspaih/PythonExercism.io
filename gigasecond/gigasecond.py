#! /usr/bin/env python3

# Exercism.io Gigasecond - Calculate the moment when someone has lived for 109
#    seconds.
# Mark Lotspaih


def add_gigasecond(birthDate):
    '''Calculate the moment when someone has lived for 10^9 seconds.'''
    import datetime
    addGigasecond = datetime.timedelta(seconds=1000000000)
    livedGigaseconds = birthDate + addGigasecond
    return livedGigaseconds
