# Create a function that returns an array of strings sorted by length in descending order.
# Keep the original order of strings with the same length.
#
# Examples:
# ["dddd","ccc","bb","a"]  == solution(["a","ccc","dddd","bb"])
# ["shortcake","apple","pie"]  == solution(["apple","pie","shortcake"])
# ["september","august","april","may"]  == solution(["may","april","september","august"])


from typing import List


def solution(words: List[str]) -> List[str]:
    return sorted(words, key=lambda x: -len(x))
