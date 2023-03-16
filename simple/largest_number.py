# Given an integer n, return the largest number that contains exactly n digits.
#
# Examples:
# 9  == solution(1)
# 99  == solution(2)
# 9999999  == solution(7)


def solution(n: int) -> int:
    largest_digit = '9'
    largest_num = int(largest_digit * n)
    return largest_num
