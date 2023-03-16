# A group of friends have decided to start a secret society. The name will be the first letter of each of their names.
# Create a function that takes an array of names and returns the name of the secret society
# sorted in alphabetical order.
#
# Examples:
# "AMS"  == solution(["Malcolm","Adam","Sarah"])
# "CHJRR"  == solution(["Harry","Ross","Chandler","Joey","Rachel"])

from typing import List


def solution(names: List[str]) -> str:
    first_letters = [name[0] for name in names]
    sorted_first_letters = sorted(first_letters)
    return ''.join(sorted_first_letters).upper()
