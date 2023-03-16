# The input contains the maximum number of dots on one end of a domino bone.
# Domino set is all possible combinations of domino bones. Output the number of dots on the domino set.
# Sample 2 -> 12, 1 -> 3 (0|1, 1|1)
#
# Examples:
# 12  == solution(2)
# 0  == solution(0)
# 3  == solution(1)
# 30  == solution(3)

from itertools import combinations_with_replacement


def solution(x: int) -> int:
    dots = [num for num in range(x + 1)]
    all_combinations = combinations_with_replacement(dots, 2)
    result = sum(list(map(sum, all_combinations)))
    return result
