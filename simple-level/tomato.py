# Count how many times word tomato occurs in string.
#
# Examples:
# 1  == solution("tomato")
# 3  == solution("tomatotomatotomato")


def solution(vegetables: str) -> int:
    keyword = 'tomato'
    return vegetables.count(keyword)
