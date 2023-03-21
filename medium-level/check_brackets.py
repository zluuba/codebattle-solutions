# Check the balance of the brackets in the expression. Brackets can be round: "()", square: "[]", curly "{}"
# and angle: "<>".
#
# Examples:
# false  == solution("( {)  } ")
# true  == solution("()[]{}<>")
# true  == solution("<(){[]}>")
# false  == solution("())")
# false  == solution("()(")
# false  == solution("{)][(}")


def solution(brackets: str) -> bool:
    open_brackets = ('(', '[', '{', '<')
    close_brackets = (')', ']', '}', '>')

    stack = []
    for bracket in brackets:
        if bracket == ' ':
            continue
        elif bracket in open_brackets:
            stack.append(bracket)
        elif stack and stack[-1] == open_brackets[close_brackets.index(bracket)]:
            stack.pop()
        else:
            return False

    return True if not stack else False
