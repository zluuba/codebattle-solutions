# Implement function that take three numbers and returns sum of squares of two biggest ones.
#
# Examples:
# 13  == solution(1, 2, 3)
# 2  == solution(1, 1, 1)
# 8  == solution(1, 2, 2)
# 45  == solution(6, 3, 2)
# 41  == solution(2, 4, 5)


def solution(a: int, b: int, c: int) -> int:
    biggest = sorted([a, b, c], reverse=True)
    return biggest[0] ** 2 + biggest[1] ** 2
