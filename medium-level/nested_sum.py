# Calculate sum of two-dimensial array.
#
# Examples:
# -33  == solution([[-1,-28,14],[-16,1,30,-12,8],[-17,10],[-26,2,-3,-9,14]])
# 86  == solution([[16],[16,20,24,8],[1],[-28],[13,16]])
# -22  == solution([[-1,11,-3,-30,-1],[2]])


from typing import List


def solution(arr: List[List[int]]) -> int:
    return sum([sum(lst) for lst in arr])
