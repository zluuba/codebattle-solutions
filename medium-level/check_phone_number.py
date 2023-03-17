# Write a function to validate some strings that could potentially represent phone numbers.
#
# Examples:
# true  == solution("5555555555")
# true  == solution("555555555")
# true  == solution("555-5555")
# true  == solution("(555) 555-5555")
# true  == solution("(555) 555-555")
# true  == solution("(555) 555-555-5555")
# false  == solution("(555) 555a-555-5555")
# false  == solution("555*-555-5555")
# false  == solution("55a-555-5555")
# true  == solution("55-55-55")
# true  == solution("55 55 55")

import re


def solution(candidate: str) -> bool:
    matches = re.findall("^[(\d\s][-)\d\s]+$", candidate)
    return matches != []


# Alternative solution with more accurate regex-expression
def solution2(candidate: str) -> bool:
    matches = re.findall("^((8|0|((\+|00)\d{1,2}))[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{6,12}$", candidate)
    return matches != []
