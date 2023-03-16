# Given a sentence (as string), return an array of words which are longer than the average length of all the words.
# Words a separated by a whitespace. If there is a trailing period (dot), it should be omittied.
# If there is no result, return ["there is no result!"]
#
# Examples:
# ["there is no result!"]  == solution("test")
# ["This","sample","string"]  == solution("This is a sample string")
# ["another","sample"]  == solution("Some another sample")

from typing import List


def solution(sentence: str) -> List[str]:
    lst = sentence.strip('.').split()
    length = len(lst)

    if length < 2:
        return ['there is no result!']

    medium = sum(map(len, lst)) // length
    return list(filter(lambda word: len(word) > medium, lst))
