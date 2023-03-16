# Given array with strings, that represents combination of first name and last name.
# Create a function, that extracts first and last name in hash-map and adds it to result array.
# Keep order the same.

# Examples:
# [{"first": "John","last": "Doe"}]  == solution(["John Doe"])
# [{"first": "Harold","last": "Abelson"}, {"first": "Julie", "last": "Sussman"}] == solution(["Harold Abelson",
# "Julie Sussman"])

from typing import List, Dict


def solution(names: List[str]) -> List[Dict[str, str]]:
    result = []
    for name in names:
        first, last = name.split()
        split_name = {'first': first, 'last': last}
        result.append(split_name)

    return result
