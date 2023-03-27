# Create a function, thats check if subnet contains in address, which contains IPv4 address and subnet mask.
#
# Examples:
# true  == solution("192.168.100.1/12", "192.168.100.5")
# false  == solution("198.201.121.1/15", "192.11.100.255")
# true  == solution("201.224.121.12/30", "201.224.121.15")


def solution(address: str, subnet: str) -> bool:
    ip, mask = address.split('/')

    if set(ip.split('.')) & set(subnet.split('.')):
        return True
    return False
