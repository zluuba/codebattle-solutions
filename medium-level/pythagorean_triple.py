# Check if 3 given integers form a Pythagorian Triplet. Pythagorian Triplet is a triplet of numbers,
# such that x^2 + y^2 = z^2
#
# Examples:
# true  == solution([12,5,13])
# true  == solution([3,5,4])
# false  == solution([8,9,7])
# false  == solution([8,3,6])


from typing import List


def solution(nums: List[int]) -> bool:
    x, y, z = sorted(nums)
    return (x ** 2 + y ** 2) == z ** 2
