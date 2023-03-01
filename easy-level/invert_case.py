# Implement a function that changes the case of each letter in the string to the opposite.
#
# Examples:
# "hELLO, wORLD."  == solution("Hello, World.")
# "i lOVE clojure!"  == solution("I Love CLOJURE!")
# "mIxEd CaSe"  == solution("MiXeD cAsE")
# "FRONTEND? what IS it?"  == solution("frontend? WHAT is IT?")


def solution(str: str) -> str:
    return str.swapcase()
