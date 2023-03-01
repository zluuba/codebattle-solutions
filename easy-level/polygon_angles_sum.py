# Given an n-sided regular polygon n. Calculate total sum of internal angles (in degrees).
#
# Examples:
# 180  == solution(3)
# 360  == solution(4)
# 720  == solution(6)


def solution(n: int) -> int:
    return (n - 2) * 180
