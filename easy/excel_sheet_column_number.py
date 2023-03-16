# Given a column title (as it appears in an Excel sheet), return its corresponding column number.
# For example: A -> 1, B -> 2, C -> 3, ... Z -> 26, AA -> 27, AB -> 28
#
# Examples:
# 666  == solution("YP")
# 26  == solution("Z")
# 1  == solution("A")
# 2458  == solution("CPN")
# 24568  == solution("AJHX")


def solution(title: str) -> int:
    if len(title) == 1:
        return ord(title) - 64

    result, curr_position = 0, 0
    for char in title[::-1]:
        digit = ord(char) - 64
        result += digit * 26 ** curr_position
        curr_position += 1

    return result
