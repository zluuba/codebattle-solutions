# Create a function that takes an array of numbers and return both the minimum and maximum numbers.
#
# Examples:
# [-3,22]  == solution([-3,2,10,22])
# [0,1]  == solution([0,0,0,1,1,1])
# [30,32]  == solution([30,30,31,32])


from typing import List


def solution(numbers: List[int]) -> List[int]:
    minimum = min(numbers)
    maximum = max(numbers)
    return [minimum, maximum]
