# https://py.checkio.org/en/mission/sun-angle/

def sun_angle(time):
    minutes = int(time[:2]) * 60 + int(time[3:])
    if minutes < 360 or minutes > 720:
        return "I don't see the sun!"
    else:
        return 0.25 * (minutes - 360)


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
