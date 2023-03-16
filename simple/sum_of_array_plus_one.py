# Given an array of integers, return the sum of integers after adding 1 to each one.
#
# Examples:
# 16  == solution([12,-3,0,3])
# 14  == solution([1,2,3,4])


from typing import List


def solution(arr: List[int]) -> int:
    add_one = [num + 1 for num in arr]
    return sum(add_one)

# or -----
# def solution(arr: List[int]) -> int:
#     return sum(arr) + len(arr)
