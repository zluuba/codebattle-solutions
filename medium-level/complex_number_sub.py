# Implement a function that calculates difference of two complex numbers. Return result as array where
# first number is real part and second number is imaginary part.

# Examples:
# [2,-1]  == solution([5,-2], [3,-1])
# [-5,2]  == solution([-3,3], [2,1])
# [1,3]  == solution([3,4], [2,1])
# [-1,-3]  == solution([-3,-4], [-2,-1])

from typing import List


def solution(first: List[int], second: List[int]) -> List[int]:
    real1, img1 = first[0], first[1]
    real2, img2 = second[0], second[1]

    real = real1 - real2
    imaginary = img1 - img2
    return [real, imaginary]
