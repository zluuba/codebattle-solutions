# Given two integer numbers. Create a simple calculator that supports next operations: add, substract, pow, multiply.
#
# Examples:
# 11  == solution(1, 10, "+")
# -3  == solution(2, 5, "-")
# -5  == solution(-1, 5, "*")
# 5  == solution(1, 5, "*")
# 100  == solution(10, 2, "^")


def solution(first: int, second: int, operation: str) -> int:
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    return first ** second
