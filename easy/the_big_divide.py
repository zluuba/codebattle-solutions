# Calculate the sum of all natural numbers smaller than n (first argument) which are divisible by a or/and b
# (second and third arguments) without remainder.
#
# Examples:
# 23  == solution(10, 3, 5)
# 0  == solution(3, 17, 11)
# 233168  == solution(1000, 3, 5)


def solution(n: int, a: int, b: int) -> int:
    result = 0

    for i in range(n):
        if i % a == 0 or i % b == 0:
            result += i

    return result


# Alternative solution
def solution2(n: int, a: int, b: int) -> int:
    result = [i for i in range(n) if i % a == 0 or i % b == 0]
    return sum(result)
