# Concatenate 2 strings by characters, one by one. In other words, take the 1st char from the first string,
# then 1st char from the second string, then 2nd char from the first string, then 2nd char from the second string,
# and so on. If one string ends before the other, just continue with the remaining characters.
#
# Examples:
# "awbxcydz"  == solution("abcd", "wxyz")
# "axbyczd"  == solution("abcd", "xyz")
# "wdoorudbleword"  == solution("word", "doubleword")
# "abcdefgh"  == solution("aceg", "bdfh")


def solution(str1: str, str2: str) -> str:
    length = min(len(str1), len(str2))

    result = ''
    ind = 0
    for i in range(length):
        result += str1[i]
        result += str2[i]
        ind = i

    remainder = str1[ind + 1:] if len(str1) > len(str2) else str2[ind + 1:]
    return result + remainder
