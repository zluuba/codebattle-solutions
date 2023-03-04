# Create a function that adds the correct parity bit to a binary string.
# Parity bits are used as a very simple checksum to ensure that binary data isn't corrupted during transit.
# Here's how they work:
#
# - If a binary string has an odd number of 1's, the parity bit is a 1.
# - If a binary string has an even number of 1's, the parity bit is a 0.
# The parity bit is appended to the end of the binary string.

# Examples:
# "1011010"  == solution("101101")
# "10110111"  == solution("1011011")
# "11111111"  == solution("1111111")
# "1010"  == solution("101")


def solution(bitstring: str) -> str:
    if bitstring.count('1') % 2 == 0:
        return bitstring + '0'
    return bitstring + '1'
