# Find how many pairs X, Y there are in the array, such that abs(X-Y) is equal to the first argument.

# Examples:
# 3  == solution(4, [1,1,5,6,9,16,27])
# 4  == solution(2, [1,1,3,3])
# 3  == solution(12, [6,6,2,-11,9,-3,9,12,0,-11,7])
# 3  == solution(7, [1,5,-2,2,-5,7,-2])
# 2  == solution(1, [-1,1,0])
# 4  == solution(3, [-2,0,-2,3,3,1])

from typing import List


def solution(differ: int, b: List[int]) -> int:
    length = len(b)
    result = 0

    for i in range(length):
        for j in range(i, length):
            if i != j and abs(b[i] - b[j]) == differ:
                result += 1

    return result
