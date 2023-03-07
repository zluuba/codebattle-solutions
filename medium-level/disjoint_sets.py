# Given two sets represented by two arrays, check if the given two sets are disjoint or not.
# Given arrays have no duplicates.
#
# Examples:
# true  == solution([12,34,11,9,3], [7,2,1,5])
# false  == solution([12,34,11,9,3], [2,1,3,5])
# true  == solution([15,16,7,2,1], [14,20,8,6,0])
# false  == solution([1,2,4,5,8,9], [2,1,3,5,9])


from typing import List


def solution(arr1: List[int], arr2: List[int]) -> bool:
    return not (set(arr1) & set(arr2))
