# Write function that, given a lowercase word, returns the degree of the word if it's a garland word and 0 otherwise.
# A garland word is one that starts and ends with the same N letters in the same order, for some N greater than 0,
# but less that the length of the word.
#
# Examples:
# 2  == solution("onion")
# 1  == solution("ceramic")
# 0  == solution("programmer")
# 4  == solution("alfalfa")
# 4  == solution("abracadabra")
# 5  == solution("undergrounder")


def solution(word: str) -> int:
    result = 0
    for i in range(len(word)):
        if word[:i] == word[-i:]:
            result = i

    return result
