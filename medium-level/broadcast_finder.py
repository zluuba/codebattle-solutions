# Create a function, thats finds broadcast network address in address, which contains IPv4 address and subnet mask.
# If adrerss invalid, return "invalid adress!!111"

# Examples:
# "192.175.255.255"  == solution("192.168.100.1/12")
# "198.201.255.255"  == solution("198.201.121.1/15")
# "201.224.121.15"  == solution("201.224.121.12/30")
# "invalid adress!!111"  == solution("0.168.100.1/33")

import ipaddress


def solution(address: str) -> str:
    ip, mask = address.split('/')

    try:
        if 0 < int(mask) > 32:
            raise Exception
        net = ipaddress.ip_network(address, False)
        return str(net.broadcast_address)
    except:
        return "invalid adress!!111"
