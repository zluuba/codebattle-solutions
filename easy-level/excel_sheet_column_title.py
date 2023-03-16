# Given a positive integer, return its corresponding column title as it appears in an Excel sheet.
# For example: 1 -> A, 2 -> B, 3 -> C, ..., 26 -> Z, 27 -> AA, 28 -> AB
#
# Examples:
# "YP"  == solution(666)
# "A"  == solution(1)
# "Z"  == solution(26)
# "CPN"  == solution(2458)
# "AJHX"  == solution(24568)

from string import ascii_uppercase


def solution(num: int) -> str:
    alphabet = ascii_uppercase
    result = ''

    while num:
        num = num - 1
        result = alphabet[num % 26] + result
        num = num // 26

    return result
