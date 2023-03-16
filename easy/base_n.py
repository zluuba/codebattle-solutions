# Check whether the number can be a n-nary number (in other words, whether the number is in base-n for n < 10).
#
# Examples:
# false  == solution(6161, 3)
# true  == solution(1010, 2)
# false  == solution(2341, 4)
# true  == solution(5511, 8)


def solution(num: int, base: int) -> bool:
    return all(n < str(base) for n in str(num))
