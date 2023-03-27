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
    num1 = complex(*first)
    num2 = complex(*second)

    real = (num1.real * num2.real) - (num1.imag * num2.imag)
    imaginary = (num1.real * num2.imag) + (num1.imag * num2.real)

    return [int(real), int(imaginary)]
