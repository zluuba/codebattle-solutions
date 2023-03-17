# Check if a given pair of numbers is a Ruth–Aaron pair. A Ruth–Aaron pair consists of two consecutive integers
# (e.g. 714 and 715) for which the sums of the prime factors of each integer are equal.
# When calculating the sum, take into account the repeating factors.
#
# Examples:
# true  == solution([8,9])
# true  == solution([5,6])
# true  == solution([77,78])
# false  == solution([20,21])

from typing import List


def solution(arr: List[int]) -> bool:

    def find_prime_factors(num):
        primf, i = [], 2
        while i * i <= num:
            while num % i == 0:
                primf.append(i)
                num = num / i
            i += 1
        if num > 1:
            primf.append(num)
        return primf

    num1, num2 = arr[0], arr[1]
    primf_num1 = find_prime_factors(num1)
    primf_num2 = find_prime_factors(num2)

    return sum(primf_num1) == sum(primf_num2)
