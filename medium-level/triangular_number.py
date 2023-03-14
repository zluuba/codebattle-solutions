# Triangular Number Sequence is generated from a pattern of dots that form a triangle.
# The first 5 numbers of the sequence, or dots, are: 1, 3, 6, 10, 15 This means that the first triangle has
# just one dot, the second one has three dots, the third one has 6 dots and so on.
# Write a function that gives the number of dots with its corresponding triangle number of the sequence.
#
# Examples:
# 1  == solution(1)
# 21  == solution(6)
# 23220  == solution(215)


def solution(n: int) -> int:
    dots = [i for i in range(n+1)]
    return sum(dots)


# Alternative solution
def solution2(n: int) -> int:
    result = 0
    dots = 1

    for i in range(n):
        result += dots
        dots += 1

    return result
