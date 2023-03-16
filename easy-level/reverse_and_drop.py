# You are given a string of words. Drop each word with odd length and reverse each word with even one.
#
# Examples:
# "eb"  == solution("learn clojure be happy")
# "emos tset htiw htgnel"  == solution("some test words with odd length")


def solution(sentence: str) -> str:
    result = [word[::-1] for word in sentence.split() if len(word) % 2 == 0]
    return ' '.join(result)
