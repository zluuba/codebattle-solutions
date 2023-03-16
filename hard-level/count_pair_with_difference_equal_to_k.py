# Given an integer array and a positive integer k, count all distinct pairs with difference equal to k.
#
# Examples:
# 2  == solution([1,5,3,4,2], 3)
# 5  == solution([8,12,16,4,0,20], 4)
# 7  == solution([1,4,3,0,2,5,7,8,9,6], 3)
# 3  == solution([1,2,3,4,4,2,2,1], 0)

from typing import List


def solution(pairs: List[int], k: int) -> int:
    p = []
    for i in range(len(pairs)):
        for j in range(len(pairs)):
            if i != j and ((pairs[i], pairs[j]) not in p and (pairs[j], pairs[i]) not in p):
                pair = (pairs[i], pairs[j])
                p.append(pair)

    res = list(map(lambda x: abs(x[0] - x[1]), p))
    return res.count(k)
