# Determine if the year is a leap year. Leap years are all divisible by 4,
# a year that is evenly divisible by 100 (for example, 1900) is a leap year only if it is also evenly divisible by 400.
#
# Examples:
# true  == solution(2012)
# false  == solution(1913)
# true  == solution(1804)
# true  == solution(2000)
# false  == solution(2100)
# true  == solution(2020)


def solution(year: int) -> bool:
    if year % 400 == 0 and year % 100 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    return False
