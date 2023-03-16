# Drop every N'th element from a list.
#
# Examples:
# [0,2,4,6,8]  == solution(2, [0,1,2,3,4,5,6,7,8,9])
# [0,1,2,3]  == solution(5, [0,1,2,3])


from typing import List


def solution(num: int, list: List[int]) -> List[int]:
    return [n for ind, n in enumerate(list, 1) if ind % num != 0]
