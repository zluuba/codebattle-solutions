# Provide the word in the form of an acronym composed of the first letter,
# the number of letters in the word minus 2 and the last letter of the word.
#
# Examples:
# "L10n"  == solution("Localization")
# "M17n"  == solution("Multilingualization")
# "I18n"  == solution("Internationalization")


def solution(s: str) -> str:
    return s[0] + str(len(s) - 2) + s[-1]
