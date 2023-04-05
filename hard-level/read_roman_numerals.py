# Parse a Roman-numeral string and return the number it represents.
#
# Examples:
# 14  == solution("XIV")
# 827  == solution("DCCCXXVII")
# 3999  == solution("MMMCMXCIX")
# 48  == solution("XLVIII")


def solution(num: str) -> int:
    numerals = {
        'M': 1000, 'D': 500, 'C': 100,
        'L': 50, 'X': 10, 'V': 5, 'I': 1,
    }

    length = len(num)
    result = 0
    for i in range(length):
        if i < length - 1 and numerals[num[i]] < numerals[num[i + 1]]:
            result -= numerals[num[i]]
        else:
            result += numerals[num[i]]

    return result
