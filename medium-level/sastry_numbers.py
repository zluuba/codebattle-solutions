# Check if a given integer n is a Sastry number. A number n is a Sastry number
# if concatenated with n + 1 it gives a square.
#
# Examples:
# true  == solution(183)
# true  == solution(328)
# true  == solution(528)
# false  == solution(322)


def solution(number: int) -> bool:
    sastry_candidate = float(str(number) + str(number + 1))
    square = sastry_candidate ** (1 / 2)

    return square == round(square)
