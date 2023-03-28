# Check if any anagram of a given string is a palindrome.
#
# Examples:
# true  == solution("abcabc")
# true  == solution("")
# true  == solution("a")
# true  == solution("aa")
# true  == solution("aab")
# true  == solution("aabb")
# true  == solution("aabbc")
# false  == solution("ab")
# false  == solution("aabbcd")
# false  == solution("aaabbb")


def solution(s: str) -> bool:
    char_counter = [s.count(char) for char in set(s)]
    odds = [i for i in char_counter if i % 2 != 0]

    if len(odds) < 2:
        return True
    return False
