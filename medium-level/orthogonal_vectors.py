# Create a function that takes two vectors and checks if them are orthogonal or not.
# Two vectors are orthogonal if their dot product is equal to zero.
#
# Examples:
# true  == solution([1,2], [2,-1])
# true  == solution([3,-3], [3,3])
# false  == solution([3,-1], [3,0])

from typing import List


def solution(vec1: List[int], vec2: List[int]) -> bool:
    x1, y1 = vec1
    x2, y2 = vec2

    if x1 * x2 + y1 * y2 == 0:
        return True
    return False
