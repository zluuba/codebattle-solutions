# Create a function that finds how many prime numbers are in a sequence from zero to a given integer, inclusive.
#
# Examples:
# 0  == solution(0)
# 4  == solution(10)
# 9  == solution(25)
# 7  == solution(17)
# 25  == solution(100)


def solution(number: int) -> int:
    def is_prime(num):
        for divider in range(2, (num // 2) + 1):
            if num % divider == 0:
                return False
        return True

    if number < 2:
        return 0

    prime_numbers = [i for i in range(2, number + 1) if is_prime(i)]
    return len(prime_numbers)
