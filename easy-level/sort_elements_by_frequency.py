# Given an array of integers, sort the array according to frequency of elements. Most frequent numbers come first.
# If several groups of the same size exist, they should appear in the order of corresponding numbers in the input array.
#
# Examples:
# [3,3,3,3,2,2,2,12,12,4,5]  == solution([2,3,2,4,5,12,2,3,3,3,12])
# [2,2,2,3,4]  == solution([2,2,2,3,4])
# [1,1,1,1,2,2,3,3,4]  == solution([1,2,1,2,1,4,3,3,1])
# [8,8,7,7,2,2,1,1,9,9,6]  == solution([8,6,8,7,2,2,7,1,9,9,1])
# [4,4,9,-11,1,12,-10,3,-3,6,5,2,-9]  == solution([9,-11,1,12,-10,3,-3,6,5,2,-9,4,4])


from typing import List
from collections import Counter


def solution(arr: List[int]) -> List[int]:
    return [item for items, count in Counter(arr).most_common() for item in [items] * count]
