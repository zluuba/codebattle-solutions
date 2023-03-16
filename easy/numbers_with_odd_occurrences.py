# Find numbers which have odd occurrences in array.
#
# Examples:
# [34,45]  == solution([12,23,34,12,12,23,12,45])
# [4,100,5000]  == solution([4,4,100,5000,4,4,4,4,4,100,100])
# [6,5,9,21]  == solution([3,3,4,6,4,5,9,9,21,9])
# [8,16,23,42]  == solution([4,8,15,16,23,42,4,15,42,42])

from typing import List


def solution(arr: List[int]) -> List[int]:
    arr_dict = {}

    for num in arr:
        if num not in arr_dict:
            arr_dict[num] = 0
        arr_dict[num] += 1

    result = [key for key, value in arr_dict.items() if value % 2 != 0]
    return result
