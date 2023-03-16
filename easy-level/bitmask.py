# Create a function that applies bitmask to bitstring. Use logical operator AND.
#
# Examples:
# "101101"  == solution("101101", "101101")
# "0011"  == solution("1011", "0111")
# "100"  == solution("101", "110")


def solution(bitstring: str, bitmask: str) -> str:
    result = [int(bitstring[i]) & int(bitmask[i]) for i in range(len(bitstring))]
    return ''.join(map(str, result))
