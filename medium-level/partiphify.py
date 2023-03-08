# Create a function that will divide the list by a specified number of parts.
#
# Examples:
# [[1],[]]  == solution([1], 2)
# [[1],[2],[3]]  == solution([1,2,3], 3)
# [[1,2,3],[4,5]]  == solution([1,2,3,4,5], 2)

from typing import List
import math


def solution(numbers: List[int], parts: int) -> List[List[int]]:
    size = math.ceil(len(numbers) / parts)
    result = []
    index = 0
    while index < len(numbers):
        result.append(numbers[index:index + size])
        index += size

    if len(numbers) < parts:
        result.append([])

    return result


# def solution(numbers: List[int], parts: int) -> List[List[int]]:
#     length = len(numbers)
#
#     if length <= parts:
#         result = [[numbers[num]] if num < length else [] for num in range(parts)]
#         while result.count([]) > 1:
#             result.pop()
#         return result
#
#     chunk = math.ceil(length / parts)
#     result = []
#     for i in range(parts):
#         tmp = []
#         for j in range(chunk):
#             if numbers:
#                 tmp.append(numbers.pop(0))
#         result.append(tmp)
#
#     return result
