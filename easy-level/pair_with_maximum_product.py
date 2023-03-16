# Given an array with both positive and negative integers, return a pair of integers that, when multiplied,
# would produce the largest possible number. An element can only be used once, in other words,
# you cannot multiply a number by itself. Elements of the pair should be arranged in ascending order.
#
# Examples:
# [-4,-3]  == solution([-1,-2,-4,-3,0,3,2,1])
# [6,7]  == solution([1,4,3,6,7,0])
# [-5,-4]  == solution([-1,-3,-4,2,0,-5])


from typing import List


def solution(arr: List[int]) -> List[int]:
    pair = []
    multiply = 0

    for ind, i in enumerate(arr):
        for ind2, j in enumerate(arr):
            if (ind != ind2) and (i * j > multiply):
                pair = [i, j]
                multiply = i * j

    return sorted(pair)
