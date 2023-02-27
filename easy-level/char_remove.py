# Write a function that removes every character from every string in array.
#
# Examples:
# ["es","wo","example"]  == solution(["test","two","example"], "t")
# ["earn","cojure","be","happy"]  == solution(["learn","clojure","be","happy"], "l")
# ["foo","bar","frontend"]  == solution(["foo","bar","frontend"], "z")


from typing import List


def solution(words: List[str], character: str) -> List[str]:
    result = []

    for word in words:
        new_word = ''
        for char in word:
            if char != character:
                new_word += char
        result.append(new_word)

    return result
