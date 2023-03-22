# Given a string with words separated in different ways, return an underscored, lowercase form.
#
# Examples:
# "active_model/errors"  == solution("ActiveModel::Errors")
# "hello_how_are_you"  == solution("HelloHowAreYou")
# "my_name_is_bond_james_bond"  == solution("MyNAMEIsBOND-JamesBond")
# "main_company/best_main_user"  == solution("MAINCompany::BEST-MAINUser")
import re


def solution(str: str) -> str:
    res = re.sub(r'-', '_', str)
    res = re.sub(r'([a-z])([A-Z])', r"\1_\2", res)
    res = re.sub(r'([A-Z+])([A-Z][a-z])', r'\1_\2', res)
    res = re.sub(r'::', '/', res)

    return res.lower()


# Alternative solution. Without regex

def solution2(str: str) -> str:
    while '::' in str:
        str = str.replace('::', '/')

    underscore_str = ''
    for char in str:
        if not char.isalpha() and char != '/':
            char = '_'
        underscore_str += char

    result = []
    word = ''
    for char in underscore_str:
        if not word and char == char.upper():
            word += char
        elif char != char.upper() and len(word) == 1:
            word += char
        elif char != char.upper() and word != word.upper():
            word += char
        elif word and word != word.upper() and char == char.upper():
            result.append(word.lower())
            word = char
        elif word and word == word.upper() and char == char.upper():
            word += char
        elif word and word == word.upper() and char != char.upper():
            last_char = word[-1]
            result.append(word[:-1].lower())
            word = last_char + char

    if word:
        result.append(word.lower())

    result_word = '_'.join(result)

    while '__' in result_word or '_/_' in result_word or '_/' in result_word:
        result_word = result_word.replace('__', '_').replace('_/_', '/').replace('_/', '/')

    return result_word
