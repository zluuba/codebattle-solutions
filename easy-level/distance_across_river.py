# Compute the distance a boat travels across a river, given the width of the river,
# the boat's speed perpendicular to the river, and the river's speed. Use ceil rounding.
#
# Examples:
# 5.0  == solution(3, 6, 8)
# 10.0  == solution(10, 10, 0)
# 5.0  == solution(4, 3, 2)


import math


def solution(width: int, boat: int, river: int) -> float:
    t = width / boat
    sm = t * river
    result = (width * width + sm * sm) ** 0.5
    return math.ceil(result)
