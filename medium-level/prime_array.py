# Generate the array of first n prime numbers.

# Examples:
# [2,3,5,7,11,13,17,19,23,29]  == solution(10)
# [2,3,5,7]  == solution(4)
# [2]  == solution(1)

from typing import List


def solution(n: int) -> List[int]:
    def is_prime(num):
        for divider in range(2, num // 2 + 1):
            if num % divider == 0:
                return False
        return True

    prime_numbers = []
    number = 2
    while len(prime_numbers) < n:
        if is_prime(number):
            prime_numbers.append(number)
        number += 1

    return prime_numbers
