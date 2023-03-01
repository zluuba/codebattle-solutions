# Determine if a given integer is a power of two.
#
# Examples:
# true  == solution(16)
# false  == solution(20)
# true  == solution(1)
# false  == solution(258)
# false  == solution(0)


def solution(num: int) -> bool:
    n = 1
    while n < num:
        n = n * 2

    if n == num:
        return True
    return False
