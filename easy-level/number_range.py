# Create a function that validates whether a number n is inclusively within the bounds of lower and upper.
#
# Examples:
# true  == solution(3, 1, 9)
# false  == solution(7, 1, 6)
# true  == solution(11, 1, 20)
# false  == solution(4, 11, 15)


def solution(num: int, lower: int, upper: int) -> bool:
    return lower <= num <= upper
