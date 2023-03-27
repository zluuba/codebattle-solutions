# Given an integer x, return the sum x + xx + xxx (x times) as a string. For example, for 2: 2 + 22 = 24.
#
# Examples:
# "369"  == solution(3)
# "61725"  == solution(5)
# "740736"  == solution(6)
# "98765424"  == solution(8)


def solution(num: int) -> str:
    result = [int(str(num) * i) for i in range(1, num + 1)]
    return str(sum(result))
