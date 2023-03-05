# Implement a function that calculates the volume of pizza. Round final result.
#
# Examples:
# 3  == solution(1, 1)
# 308  == solution(7, 2)
# 942  == solution(10, 3)


import math


def solution(radius: int, height: int) -> int:
    square = math.pi * (radius ** 2)
    volume = square * height
    return round(volume)
