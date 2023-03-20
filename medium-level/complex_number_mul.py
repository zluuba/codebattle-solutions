# Implement a function that multiply two complex numbers. Return result as array where first number is real part
# and second number is imaginary part.
#
# Examples:
# [1,-7]  == solution([1,-2], [3,-1])
# [-8,1]  == solution([-3,2], [2,1])
# [4,7]  == solution([3,2], [2,1])
# [-5,-1]  == solution([2,3], [-1,1])

from typing import List


def solution(first: List[int], second: List[int]) -> List[int]:
    real1, img1 = first[0], first[1]
    real2, img2 = second[0], second[1]

    real = (real1 * real2) - (img1 * img2)
    imaginary = (real1 * img2) + (img1 * real2)
    return [real, imaginary]
