# Credit card numbers can be validated with a process called the Luhn algorithm.
# Simply stated, the Luhn algorithm works like this:
# 1. From the rightmost digit, which is the check digit, moving left,
#   double the value of every second digit; if the product of this doubling operation is greater than 9
#   (e.g., 8 × 2 = 16), then sum the digits of the products (e.g., 16: 1 + 6 = 7, 18: 1 + 8 = 9).
# 2. Take the sum of all the digits.
# 3. If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according
#   to the Luhn formula; else it is not valid.

# Examples:
# true  == solution("4408041234567893")
# false  == solution("1234567890123456")
# false  == solution("4408042234567893")
# true  == solution("38520000023237")
# true  == solution("4222222222222")


def solution(arr: str) -> bool:
    result = []
    for ind, n in enumerate(arr[::-1]):
        num = int(n)

        if ind % 2 != 0:
            num = num * 2
            if len(str(num)) > 1:
                num = sum([int(i) for i in str(num)])

        result.append(num)

    return str(sum(result))[-1] == '0'
