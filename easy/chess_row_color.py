# Identify the color of a square of the chessboard. Square A1 is black.
#
# Examples:
# "black"  == solution("A", 1)
# "black"  == solution("H", 8)
# "black"  == solution("D", 4)
# "black"  == solution("G", 7)
# "white"  == solution("A", 8)
# "white"  == solution("H", 1)
# "white"  == solution("E", 8)
# "white"  == solution("E", 4)


def solution(row: str, column: int) -> str:
    field = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4,
        'E': 5, 'F': 6, 'G': 7, 'H': 8
    }

    if (field[row] % 2 == 0 and column % 2 == 0) or \
            (field[row] % 2 != 0 and column % 2 != 0):
        return 'black'
    return 'white'
