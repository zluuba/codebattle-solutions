# Write a method/function that takes a number (int) as input, and outputs a word in the plural or singular (only simple cases) corresponding to the specified number.
#
# Examples:
# "1 computer"  == solution(1)
# "512 computers"  == solution(512)
# "1024 computers"  == solution(1024)


def solution(number: int) -> str:
    if number == 1:
        return "1 computer"
    return f'{number} computers'
