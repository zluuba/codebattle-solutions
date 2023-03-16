# Write a function that replaces every character for replacement from every string in array.
#
# Examples:
# ["desd","sdring","example"]  == solution(["test","string","example"], "t", "d")
# ["Learn","cLojure","be","happy"]  == solution(["learn","clojure","be","happy"], "l", "L")
# ["foo","bar","frontend"]  == solution(["foo","bar","frontend"], "z", "Y")


from typing import List


def solution(words: List[str], character: str, replacement: str) -> List[str]:
    result = []

    for word in words:
        new_word = ''
        for char in word:
            if char == character:
                char = replacement
            new_word += char
        result.append(new_word)

    return result
