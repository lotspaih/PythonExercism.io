#!/usr/bin/env python3

# Exercism.io Leap - Given a year, report if it is a leap year.
# Mark Lotspaih


def is_leap_year(year):
    '''Given a year, return True if it is a leap year.'''
    if year % 4 == 0:
        if not year % 100 == 0:
            return True
        elif not year % 400 == 0:
            return False
        else:
            return True
    else:
        return False
