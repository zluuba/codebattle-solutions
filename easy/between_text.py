# Write function that returns subtext from text between given patterns.
#
# Examples:
# "foo"  == solution("<a>foo</a>", "<a>", "</a>")
# "text"  == solution("this is 'text'", "'", "'")
# "oni"  == solution("xonix", "x", "x")
# "google"  == solution("www.google.com", "www.", ".com")
# " wow "  == solution("oh wow such example", "oh", "such")


def solution(str: str, left: str, right: str) -> str:
    if left not in str or right not in str:
        return ''

    l = str.find(left) + len(left)
    r = str[l+1:].find(right) + (l + 1)

    return str[l:r]
