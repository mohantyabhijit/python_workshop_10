# Write a function to return one of 3 possible results: "Low speed", "Medium speed", or "Fastspeed". If your speed is
# 60 or less, the result is "Low speed". If speed is between 61 and 80 inclusive, the result is "Medium speed". If
# speed is 81 or more, the result is "Fast speed". Unless it is your birthday (encoded as a boolean value in the
# parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.

def speed_indicator(speed, birthday):
    if not birthday:
        speeding_message(speed, 0)
    else:
        speeding_message(speed, 5)


def speeding_message(speed, excess):
    if speed <= 60 + excess:
        print("Low speed")
    elif 61 + excess < speed <= 80 + excess:
        print("Medium speed")
    elif speed >= 81 + excess:
        print("Fast speed")


isBirthday = True
person_speed = 65
speed_indicator(person_speed, isBirthday)
