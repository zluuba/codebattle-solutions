# Sort an array of integers by the number of 1's in its binary representation (in ascending order).
# If two integers have the same number of 1's in their binary representation,
# their relative order should be the same as in the original array.
#
# Examples:
# [1,2,4,3]  == solution([1,2,3,4])
# [8,9,6,7]  == solution([9,8,7,6])
# [64,5,7,255]  == solution([255,7,5,64])
# [4,2,5,7]  == solution([5,4,2,7])

from typing import List, Dict


def solution(arr: List[int]) -> List[int]:
    return sorted(arr, key=lambda num: bin(num).count('1'))
