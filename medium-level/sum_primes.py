# Return the sum of all prime numbers from 2 up to a given number, not including this number.

# Examples:
# 2  == solution(3)
# 4227  == solution(200)
# 76127  == solution(1000)


def solution(num: int) -> int:
    def is_prime(number):
        for divider in range(2, (number // 2) + 1):
            if number % divider == 0:
                return False
        return True

    result = [i for i in range(2, num) if is_prime(i)]
    return sum(result)
