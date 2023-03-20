# The sequence of Hamming numbers 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36, …
# consists of all numbers of the form 2^i·3^j·5^k where i, j and k are non-negative integers. Generate n-th number.
#
# Examples:
# 36  == solution(20)
# 5  == solution(5)
# 937500  == solution(500)
# 51200000  == solution(1000)


def solution(n: int) -> int:
    def is_hamming_numbers(x):
        if x == 1:
            return True
        while x % 2 == 0:
            x /= 2
        while x % 3 == 0:
            x /= 3
        while x % 5 == 0:
            x /= 5
        return x == 1

    counter = 1
    num = 2

    while counter < n:
        if is_hamming_numbers(num):
            counter += 1
        num += 1

    return num - 1
