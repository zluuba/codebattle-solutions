# Given an n * n * n Rubik's cube, find the number of stickers that are needed to cover the whole cube.
#
# Examples:
# 6  == solution(1)
# 24  == solution(2)
# 54  == solution(3)


def solution(num: int) -> int:
    sides = 6
    return (num ** 2) * sides
