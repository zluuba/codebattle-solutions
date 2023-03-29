# Find the largest element in the Syracuse sequence.
#
# Examples:
# 8  == solution(6)
# 26  == solution(11)
# 4616  == solution(27)


def solution(num: int) -> int:
    biggest = num

    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        biggest = max(biggest, num // 2)

    return biggest
