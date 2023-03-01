# Create a function that takes a word and determines whether or not it is plural.
# Ignore edge cases like goose and geese, fungus and fungi, etc.
#
# Examples:
# false  == solution("fork")
# true  == solution("forks")
# false  == solution("clojure")
# true  == solution("bytes")
# false  == solution("test")


def solution(word: str) -> bool:
    return word[-1] == 's'
