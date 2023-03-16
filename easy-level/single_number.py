# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Examples:
# 6  == solution([8,6,8,7,2,2,7,1,9,9,1])
# 3  == solution([2,2,3])
# 4  == solution([4,2,2,3,6,3,8,7,8,6,7])
# 5  == solution([1,3,4,3,5,6,7,1,6,7,4])

from typing import List


def solution(arr: List[int]) -> int:
    for num in set(arr):
        if arr.count(num) == 1:
            return num
