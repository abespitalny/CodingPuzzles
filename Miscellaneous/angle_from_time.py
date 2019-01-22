# given a time in 12-hour format give the angle between the hour and minute
# hands of the clock at that time
def get_angle_from_time(time):
    # parse the hour and the minutes
    time = time.split(":")
    hour = int(time[0]) % 12
    minutes = int(time[1]) % 60

    # get angle of minutes hand
    # note: 360 degrees / 60 intervals = 6 degrees
    minutes_hand_angle = minutes * 6
    # get angle of hour hand
    # note again 360/12 = 30 and 30/60 = 0.5
    hour_hand_angle = (hour * 30) + (minutes * 0.5)

    # return the angle made between the hour and minute hands
    return abs(hour_hand_angle - minutes_hand_angle)

def main():
    print(get_angle_from_time("10:03"))
    print(get_angle_from_time("2:34"))
    print(get_angle_from_time("12:00"))
    print(get_angle_from_time("12:59"))

if __name__ == '__main__':
    main()
