#! /usr/bin/env python3

# Exercism.io Meetup - Calculate the date of meetups.
# Mark Lotspaih
# UNSOLVED
# from datetime import date


def meetup_day(year, month, weekday, recurance):
    '''Calculate the date of meetups.'''
    from datetime import date
    import calendar
    monthCal = calendar.monthcalendar(year, month)
    recuranceDict = {
        '1st': monthCal[0],
        '2nd': monthCal[1],
        '3rd': monthCal[2],
        '4th': monthCal[3],
        'teenth': monthCal[2],
        'last': monthCal[4]
    }
    weekdayDict = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6
    }
    # Logic to shift to the following week if first week is a 0 for the day?
    if recuranceDict['1st'][weekdayDict[weekday]] == 0:
        recuranceDict = {
            '1st': monthCal[1],
            '2nd': monthCal[2],
            '3rd': monthCal[3],
            '4th': monthCal[4],
            'teenth': monthCal[3],
            'last': monthCal[4]
        }
        return date(
            year, month, recuranceDict[recurance][weekdayDict[weekday]])
    else:
        return date(
            year, month, recuranceDict[recurance][weekdayDict[weekday]])


# result = meetup_day(2013, 12, 'Friday', '4th')
# if result == date(2013, 12, 27):
#     print(result)
# else:
#     print('FAILED: Result was {} but should be 2013-12-27'.format(result))
