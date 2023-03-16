# Two arrays, which represent two sandwiches are given. Return whether both sandwiches use the same type of bread.
#
# Examples:
# true  == solution(["white bread","tomato","white bread"], ["white bread","chicken","white bread"])
# false  == solution(["toast","chicken","brown bread"], ["brown bread","chicken","white bread"])
# true  == solution(["toast","cheese","toast"], ["toast","ham","toast"])


from typing import List


def solution(first: List[str], second: List[str]) -> bool:
    return first[0] == second[0] and first[-1] == second[-1]
