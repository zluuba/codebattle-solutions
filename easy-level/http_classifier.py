# Return type of provided http status code. Checkout examples for types.
# If code has no classification, return "unrecognized"
#
# Examples:
# "informational"  == solution(121)
# "success"  == solution(201)
# "redirection"  == solution(333)
# "client error"  == solution(418)
# "server error"  == solution(500)


def solution(code: int) -> str:
    if 100 <= code <= 199:
        return 'informational'
    elif 200 <= code <= 299:
        return 'success'
    elif 300 <= code <= 399:
        return 'redirection'
    elif 400 <= code <= 499:
        return 'client error'
    elif 500 <= code <= 599:
        return 'server error'
    return 'unrecognized'
