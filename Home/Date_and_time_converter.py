# https://py.checkio.org/en/mission/date-and-time-converter/

from datetime import datetime


def date_time(time: str) -> str:
    date, time = time.split()
    year = int(date.split('.')[-1])
    month = int(date.split('.')[1])
    day = int(date.split('.')[0])

    hour = int(time.split(':')[0])
    minute = int(time.split(':')[1])

    if minute == 1:
        min_str = 'minute'
    else:
        min_str = 'minutes'

    if hour == 1:
        hrs_str = 'hour'
    else:
        hrs_str = 'hours'
    date_time = datetime(year, month, day, hour=hour, minute=minute)
    return date_time.strftime(f'%-d %B %Y year %-H {hrs_str} %-M {min_str}')


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
