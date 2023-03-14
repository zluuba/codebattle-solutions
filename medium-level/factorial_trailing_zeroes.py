# Return the number of trailing zeroes in n! For example, 5! = 120, the number of trailing zeros is 1; 10! = 3 628 800,
# the number of trailing zeros is 2.
#
# Examples:
# 6  == solution(28)
# 0  == solution(0)
# 1  == solution(5)
# 1  == solution(7)
# 4  == solution(23)
# 22  == solution(99)


def solution(n: int) -> int:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    factorial = str(factorial)
    factorial_without_trailing_zeroes = factorial.rstrip('0')
    return len(factorial) - len(factorial_without_trailing_zeroes)


# Alternative solution
def solution2(n: int) -> int:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    zeros = 0
    for i in str(factorial)[::-1]:
        if i == '0':
            zeros += 1
            continue
        break

    return zeros
