# Find the largest second number in array.
#
# Examples:
# 2  == solution([1,2,3])
# 1  == solution([1,-2,3])
# 0  == solution([0,0,10])
# -2  == solution([-1,-2,-3])


from typing import List


def solution(numbers: List[int]) -> int:
    return sorted(numbers)[1]
