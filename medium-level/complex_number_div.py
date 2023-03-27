# Implement a function that divide two complex numbers. Return result as array where first number
# is real part and second number is imaginary part. Use floor rounding.
#
# Examples:
# [1,2]  == solution([3,10], [3,1])
# [12,-5]  == solution([30,2], [2,1])
# [0,-7]  == solution([77,-11], [1,11])
# [-2,-1]  == solution([30,11], [-12,1])

from typing import List


def solution(first: List[int], second: List[int]) -> List[int]:
    num1 = complex(*first)
    num2 = complex(*second)

    real = ((num1.real * num2.real) + (num1.imag * num2.imag)) / \
           ((num2.real * num2.real) + (num2.imag * num2.imag))
    imag = ((num1.imag * num2.real) - (num1.real * num2.imag)) / \
           ((num2.real * num2.real) + (num2.imag * num2.imag))

    return [int(real), int(imag)]
