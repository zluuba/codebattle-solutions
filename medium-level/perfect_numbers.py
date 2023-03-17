# Determine if a given number is "perfect". Perfect number is a positive integer that is equal to the sum of its
# proper positive divisors (the sum of its positive divisors excluding the number itself).
#
# Examples:
# true  == solution(6)
# false  == solution(7)
# true  == solution(496)
# false  == solution(500)
# true  == solution(8128)


def solution(num: int) -> bool:
    divisors = []

    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)

    return num == sum(divisors)
