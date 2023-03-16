# Happy numbers are positive integers that follow a particular formula: take each individual digit, square it,
# and then sum the squares to get a new number. Repeat with the new number and eventually,
# you might get to a number whose squared sum is 1. This is a happy number. An unhappy number (or sad number) is one
# that loops endlessly. Write a function that determines if a number is happy or not.
#
# Examples:
# true  == solution(7)
# true  == solution(986543210)
# false  == solution(2)
# false  == solution(189)


def solution(n: int) -> bool:
    new_n, count = 0, 0

    while True:
        if n == 1:
            return True
        if count > 100:
            return False

        for i in str(n):
            new_n += int(i) ** 2

        count += 1
        n, new_n = new_n, 0
