# Create a function that cyclical shifts bits of bitstring for shift amount.
#
# Examples:
# "101111"  == solution("111101", 3)
# "1110"  == solution("1011", -2)
# "10100"  == solution("10010", -3)
# "10101"  == solution("10101", 5)


def solution(bitstring: str, shift: int) -> str:
    shift = abs(shift)

    return bitstring[shift:] + bitstring[:shift]
