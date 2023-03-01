# Count how many years have passed since latest millennium. For example, for 2015 the answer is 15.
#
# Examples:
# 15  == solution(2015)
# 205  == solution(10205)


def solution(year: int) -> int:
    return year % 1000
