# Given an array, return the Next Greater Element (NGE) for every element. The Next greater Element for an
# element x is the first greater element on the right side of x in array. Elements for which no greater element exist,
# consider next greater element as -1.
#
# Examples:
# [5,25,25,-1]  == solution([4,5,2,25])
# [-1,12,12,-1]  == solution([13,7,6,12])
# [6,8,12,5,5,12,-1,9,-1]  == solution([3,6,8,2,1,5,12,4,9])
# [4,2,4,-1]  == solution([3,1,2,4])

from typing import List


def solution(arr: List[int]) -> List[int]:
    result = []

    for ind, i in enumerate(arr):
        next_greater = -1
        for j in arr[ind:]:
            if j > i:
                next_greater = j
                break
        result.append(next_greater)

    return result
