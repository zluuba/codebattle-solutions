# Create a function that calculates the number of different squares in an n * n square grid.
#
# Examples:
# 5  == solution(2)
# 30  == solution(4)
# 55  == solution(5)


def solution(number: int) -> int:
    if number <= 1:
        return number

    result = number ** 2 + (solution(number - 1))
    return result
