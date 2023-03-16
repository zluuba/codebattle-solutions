# Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.
#
# Examples:
# 17  == solution(8, 10)
# 11  == solution(5, 7)
# 10  == solution(9, 2)


def solution(first: int, second: int) -> int:
    return (first + second) - 1
