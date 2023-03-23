# Create a function that takes a positive integer and returns the nth "star number".
# A star number is a centered figurate number a centered hexagram (six-pointed star),
# such as the one that Chinese checkers is played on. Note: https://en.wikipedia.org/wiki/Star_number

# Examples:
# 13  == solution(2)
# 37  == solution(3)
# 121  == solution(5)


def solution(num: int) -> int:
    return 6 * num * (num - 1) + 1
