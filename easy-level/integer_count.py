# Create a function that counts the integer's number of digits.
#
# Examples:
# 2  == solution(45)
# 3  == solution(-123)
# 5  == solution(-12345)
# 6  == solution(976543)


def solution(num: int) -> int:
    positive_str_num = str(abs(num))
    return len(positive_str_num)
