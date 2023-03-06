# Non return to zero, inverted (NRZI) is a method of mapping a binary signal to a physical signal
# for transmission over some transmission media. The two level NRZI signal has a transition at a clock boundary
# if the bit being transmitted is a logical 1, and does not have a transition if the bit being transmitted
# is a logical 0.

#     0 100 10000 100 1 1 1
#     ¯|___|¯¯¯¯¯|___|¯|_|¯

# Examples:
# "010010000100111"  == solution("¯|___|¯¯¯¯¯|___|¯|_|¯")
# "010110010"  == solution("¯|__|¯|___|¯¯")
# "010011000110"  == solution("_|¯¯¯|_|¯¯¯¯|_|¯¯")


def solution(seq: str) -> str:
    lst = seq.split('|')
    prev = lst[0][0]
    result = '0'

    for i in lst:
        if i[0] == prev:
            result += '0' * (len(i) - 1)
        else:
            result += '1' + ('0' * (len(i) - 1))
            prev = i[0]

    return result


# Alternative solution
def solution2(seq: str) -> str:
    result, ind = '', 0
    while ind < len(seq):
        if seq[ind] == '|':
            result += '1'
            ind += 1
        else:
            result += '0'
        ind += 1

    return result
