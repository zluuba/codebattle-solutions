# Write a function that takes three numbers (first operand, second operand and result) and return string
# if they should be added, subtracted or multiplied to get result.
#
# Examples:
# "addition"  == solution(10, 12, 22)
# "subtraction"  == solution(10, 5, 5)
# "multiplication"  == solution(10, 2, 20)
# "unrecognized operation!!"  == solution(33, 33, 33)


def solution(first: int, second: int, result: int) -> str:
    if first + second == result:
        return 'addition'
    elif first - second == result:
        return 'subtraction'
    elif first * second == result:
        return 'multiplication'
    return 'unrecognized operation!!'
