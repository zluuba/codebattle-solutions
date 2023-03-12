# Check if the parentheses in the expression are all balanced, so that all open parentheses are closed properly.
#
# Examples:
# false  == solution("( )  )")
# true  == solution("()")
# true  == solution(" ( )(  )")
# true  == solution("(() )")
# false  == solution(") ")
# false  == solution("(")
# false  == solution(") (")
# false  == solution("(( )")


def solution(brackets: str) -> bool:
    stack = []

    for elem in brackets:
        if elem == '(':
            stack.append(elem)
        if elem == ')':
            if not stack:
                return False
            stack.pop()

    return not stack
