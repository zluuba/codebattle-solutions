# Calculate the sum of digits of 2**n For example, 2**15 = 32768, and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# Examples:
# 13  == solution(8)
# 26  == solution(15)


def solution(n: int) -> int:
    num = 2 ** n
    result = sum(list(map(int, str(num))))
    return result
