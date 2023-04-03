# Conway's "Look and Say" sequence is a sequence of numbers in which each term "reads aloud" the digits of
# the previous term. 1 is read off as "one 1". 11 is read off as "two 1's". 21 is read off as "one 2, then one 1".
# 1211 is read off as "one 1, then one 2, then two 1's".
#
# Examples:
# "111221"  == solution("three 1, then two 2's, then one 1")
# "11"  == solution("two 1's")
# "21"  == solution("one 2, then one 1")
# "1211"  == solution("one 1, then one 2, then two 1's")


def solution(str: str) -> str:
    keywords = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
    }

    result = ''

    for i in str.split(','):
        word, n = None, None
        for j in i.split():
            if j in keywords:
                word = j
            elif j.strip("'s").isdigit():
                n = j.strip("'s")

        result += n * keywords[word]

    return result
