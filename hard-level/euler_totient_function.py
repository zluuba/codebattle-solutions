# Two numbers are coprime if their greatest common divisor equals 1.
# Implement the Euler's totient function f(x), which is defined as the number of positive integers less than x
# which are coprime to x.
#
# Examples:
# 1  == solution(1)
# 4  == solution(10)
# 16  == solution(40)
# 60  == solution(99)

import math


def solution(num):
    result = [i for i in range(1, num + 1) if math.gcd(num, i) == 1]
    return len(result)


# Alternative solution. Without math lib

def solution2(num: int) -> int:
    def is_gcd_is_one(num1, num2):
        if num1 < num2:
            num1, num2 = num2, num1
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        return num1 == 1

    result = [i for i in range(1, num + 1) if is_gcd_is_one(num, i)]
    return len(result)
