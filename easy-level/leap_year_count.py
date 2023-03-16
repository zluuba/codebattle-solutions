# Given a range of years as array of two numbers, return the number of leap years there are within the range
# (inclusive). Leap years are all divisible by 4, with the exception of centuries, which are not divisible by 400.
#
# Examples:
# 2  == solution([1980,1984])
# 7  == solution([2000,2025])
# 49  == solution([1800,2000])

from typing import List


def solution(years: List[int]) -> int:
    first_year, last_year = years

    leap_years = 0
    for year in range(first_year, last_year + 1):
        if year % 400 == 0 and year % 100 == 0:
            leap_years += 1
        elif year % 4 == 0 and year % 100 != 0:
            leap_years += 1

    return leap_years
