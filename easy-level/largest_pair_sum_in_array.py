# Given an array of integers, find the largest pair sum in it.
# For example, the largest pair sum in [12, 34, 10, 6, 40] is 74.
#
# Examples:
# 1  == solution([1])
# 11  == solution([1,2,3,4,5,6])
# 74  == solution([12,34,10,6,40])
# 80  == solution([12,40,10,6,40])
# 52  == solution([12,-34,10,6,40])


from typing import List


def solution(arr: List[int]) -> int:
    if len(arr) == 1:
        return arr[0]

    largest_first = sorted(arr, reverse=True)
    return sum(largest_first[:2])
