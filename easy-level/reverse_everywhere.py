# Reverse each character of word in array and after that reverse array itself.
#
# Examples:
# ["emosewa","si","erujolc"]  == solution(["clojure","is","awesome"])
# ["yoj","sgnirb","ybur"]  == solution(["ruby","brings","joy"])
# ["atad","elpmas","emos"]  == solution(["some","sample","data"])


from typing import List


def solution(words: List[str]) -> List[str]:
    reverse_words = []
    for word in words[::-1]:
        reverse_words.append(word[::-1])

    return reverse_words
