# Implement the function that calculates sum of two complex numbers. Return result as array where first
# number is real part and second number is imaginary part.

# Examples:
# [4,-3]  == solution([1,-2], [3,-1])
# [-1,3]  == solution([-3,2], [2,1])
# [5,3]  == solution([3,2], [2,1])
# [-5,-3]  == solution([-3,-2], [-2,-1])

from typing import List


def solution(first: List[int], second: List[int]) -> List[int]:
    num1 = complex(*first)
    num2 = complex(*second)

    real = int(num1.real + num2.real)
    imag = int(num1.imag + num2.imag)

    return [real, imag]
