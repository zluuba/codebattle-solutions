# You are given a string of words. Reverse each word with even length.
#
# Examples:
# "learn ybur eb happy"  == solution("learn ruby be happy")
# "emos tset words htiw neve htgnel"  == solution("some test words with even length")


def solution(sentence: str) -> str:
    sentence_lst = sentence.split()
    reverse_even = [word[::-1] if len(word) % 2 == 0 else word
                    for word in sentence_lst]
    return ' '.join(reverse_even)
