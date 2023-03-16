# You are given a string of words. Drop each word with odd length.
#
# Examples:
# "be"  == solution("learn clojure be happy")
# "some test with length"  == solution("some test words with odd length")


def solution(sentence: str) -> str:
    result = [word for word in sentence.split() if len(word) % 2 == 0]
    return ' '.join(result)
