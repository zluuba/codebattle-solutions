# Create a function based on the input and output. Look at the examples, there is a pattern.
# First number in range [1, 7], second in [0 8]. Operations pow, * and - can be helpful.
#
# Examples:
# 8  == solution(2, 4)
# 8  == solution(4, 2)
# -4  == solution(1, 5)
# 15  == solution(5, 2)
# 322  == solution(7, 3)


def solution(first: int, second: int) -> int:
    return pow(first, second) - first * second
