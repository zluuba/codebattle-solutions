# Given a hash map, return the keys of the elements with the smallest value. The result should be sorted alphabetically.
#
# Examples:
# ["damage","detail"]  == solution({"father":2,"detail":-7,"education":7,"morning":3,"damage":-7,"powder":5})
# ["j"]  == solution({"k":2,"h":3,"j":1})
# ["z"]  == solution({"o":0,"z":-2,"j":1})

from typing import List, Dict


def solution(h: Dict[str, int]) -> List[str]:
    minimum = min(h.values())
    result = [key for key, value in h.items() if value == minimum]
    return sorted(result)
