# Reverse input number and convert it to string. Keep number sign.
#
# Examples:
# "3214321"  == solution(1234123)
# "-54321"  == solution(-12345)
# "0"  == solution(0)


def solution(number):
    num = str(number)

    if num[0] == '-':
        return f'-{int(num[-1:0:-1])}'
    return f'{int(num[::-1])}'
