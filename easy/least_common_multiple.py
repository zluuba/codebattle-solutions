# Create a function that calculates LCM (Least Common Multiple).
#
# Examples:
# 20  == solution(4, 5)
# 12  == solution(4, 6)
# 30  == solution(10, 30)
# 160  == solution(10, 32)


def solution(x: int, y: int) -> int:
    result = x * y

    tmp = result
    while tmp > min(x, y):
        tmp -= 1
        if tmp % x == 0 and tmp % y == 0:
            result = tmp

    return result
