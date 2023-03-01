# Calculate sum of arithmetic progression from 1 to n.
#
# Examples:
# 1  == solution(1)
# 15  == solution(5)
# 1275  == solution(50)


def solution(n: int) -> int:
    return sum([n for n in range(n + 1)])
