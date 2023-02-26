# Given an array, determine if the sum of all its elements is equal to 21.
#
# Examples:
# true  == solution([3,4,5,6,3])
# true  == solution([11,10])
# false  == solution([3,11,10])
# false  == solution([10,10])


from typing import List


def solution(arr: List[int]) -> bool:
    looking_for = 21
    return sum(arr) == looking_for
