from datetime import datetime, time

def time_converter(time_to_read):
    hour, minute = time_to_read.split(':')
    hour, minute = int(hour), int(minute)
    AM_or_PM = 'p.m.' if hour >= 12 else 'a.m.'
    return time(hour=hour, minute=minute).strftime(f'%-I:%M {AM_or_PM}')

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
