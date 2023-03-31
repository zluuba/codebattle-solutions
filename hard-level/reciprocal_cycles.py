# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with
# denominators 2 to 10 are given: 1/2 = 0.5 1/3 = 0.(3) 1/4 = 0.25 1/5 = 0.2 1/6 = 0.1(6) 1/7 = 0.(142857)
# 1/8 = 0.125 1/9 = 0.(1) 1/10 = 0.1 Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle. Find the value of d < 100 for which 1/d contains the
# longest recurring cycle in its decimal fraction part.

# Examples:
# 7  == solution(10)
# 7  == solution(77)
# 81  == solution(100)


def is_recurring_cycle(remainder):
    for i in range(1, len(remainder) // 2 + 1):
        first_part = remainder[:i]
        second_part = remainder[i:i * 2]
        if first_part[:-1] == second_part[:-1]:
            if i * 2 == len(remainder) and first_part[-1] != second_part[-1]:
                return True, remainder[:i]
            if first_part == second_part and i * 2 != len(remainder):
                return True, remainder[:i]
    return False, ''


def solution(x: int) -> int:
    result = 1
    longest_recurring = 0

    for i in range(1, x + 1):
        unit_fraction = str(1 / i)
        _, remainder = unit_fraction.split(".")
        is_recurring, recurring_part = is_recurring_cycle(remainder)

        if is_recurring:
            result = i if len(recurring_part) > longest_recurring else result
            longest_recurring = max(longest_recurring, len(recurring_part))

    return result
