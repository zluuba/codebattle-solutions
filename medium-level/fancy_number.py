# Given a number, find whether it is fancy or not. A fancy number is one which when rotated 180 degrees is the same.
# When rotated, 6 becomes 9, 9 becomes 6, and 8, 1, 0 become themselves (do not change).
#
# Examples:
# true  == solution("9081806")
# true  == solution("916")
# true  == solution("9088806")
# false  == solution("121")
# false  == solution("996")
# true  == solution("96")


def solution(num_str: str) -> bool:
    rotate_dict = {'9': '6', '6': '9', '8': '8', '1': '1', '0': '0'}

    result = ''
    for num in num_str:
        if num not in rotate_dict:
            return False
        if num in rotate_dict:
            num = rotate_dict[num]
        result += num

    return num_str[::-1] == result
