# The decimal number 585 is 1001001001 in binary. It is palindromic in both bases. Find n-th palindromic number.

# Examples:
# 5  == solution(3)
# 1  == solution(1)
# 99  == solution(7)
# 39993  == solution(15)


def solution(num: int) -> int:
    palindromes = 0
    curr = 1

    while True:
        bin_curr = bin(curr).lstrip('0b')
        str_curr = str(curr)
        if bin_curr == bin_curr[::-1] and str_curr == str_curr[::-1]:
            palindromes += 1

        if palindromes == num:
            return curr

        curr += 1
