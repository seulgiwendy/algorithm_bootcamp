def solution(year):

    if year % 4 == 0 and year % 100 != 0:
        return "Leap Year"

    elif year % 400 == 0:
        return "Leap Year"

    return "Not Leap Year"

