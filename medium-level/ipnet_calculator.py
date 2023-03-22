# Create a function, thats calculates how much network contains in address, which contains IPv4 and subnet mask.

# Examples:
# 1048576  == solution("192.168.100.1/12")
# 131072  == solution("198.201.121.1/15")
# 4  == solution("201.224.121.12/30")


def solution(address: str) -> int:
    ip, mask = address.split('/')
    return 2 ** (32 - int(mask))
