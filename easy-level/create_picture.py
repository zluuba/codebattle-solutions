# Given an array of words, write a function, that return picture (array) with borders made
# from asterisks * using longest words.
#
# Examples:
# ["*****","*def*","*****"]  == solution(["a","bc","def"])
# ["******","*some*","*word*","******"]  == solution(["some","word","foo","bar"])

from typing import List


def solution(words: List[str]) -> List[str]:
    max_length = max([len(word) for word in words])
    border = "*" * (max_length + 2)
    starred_max_length_words = [f"*{word}*" for word in words if len(word) == max_length]

    return [border] + starred_max_length_words + [border]
