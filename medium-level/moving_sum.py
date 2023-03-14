# Return the 'sliding sums' array of numbers with window size equal to window.
# For example, the sums of array [1 2 3 4 5] with window 2 will be [(1 + 2) (2 + 3) (3 + 4) (4 + 5)] -> [3 5 7 9].
# If the size of the window is larger than the size of the array, return the array with the sum of all the numbers.
#
# Examples:
# [3,5,7,9]  == solution([1,2,3,4,5], 2)
# [6,9,12]  == solution([1,2,3,4,5], 3)
# [10,14]  == solution([1,2,3,4,5], 4)
# [15]  == solution([1,2,3,4,5], 6)

from typing import List


def solution(numbers: List[int], window: int) -> List[int]:
    if len(numbers) <= window:
        return [sum(numbers)]

    result = []
    for i in range(len(numbers) - window + 1):
        num = [numbers[i + j] for j in range(window)]
        result.append(sum(num))

    return result
