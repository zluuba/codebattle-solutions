# Write a function that checks each move of the game tic-tac-toe.
# The function takes the current state of the field as a two-dimensional array. If player 'X' won, returns 'X won',
# player 'O' won - return 'O won'. If no one has won yet, return 'Next'. If the field is full,
# but no one has won return 'Game over'
#
# Examples:
# "X won"  == solution([["X","O","X"],["O","X","O"],["_","_","X"]])
# "O won"  == solution([["X","X","O"],["_","O","_"],["O","X","O"]])
# "Next"  == solution([["_","O","X"],["X","_","_"],["_","_","O"]])
# "Game over"  == solution([["X","O","X"],["O","X","X"],["O","X","O"]])

from typing import List


def solution(field: List[List[str]]) -> str:
    x, o = "X", "O"
    no_more_moves = True

    for i in range(3):
        if no_more_moves and field[i].count('_') > 0:
            no_more_moves = False

        if len(set(field[i])) == 1:
            return f"{x} won" if field[i][0] == x else f"{o} won"

        elif len({field[0][i], field[1][i], field[2][i]}) == 1:
            return f"{x} won" if field[0][i] == x else f"{o} won"
        elif len({field[0][0], field[1][1], field[2][2]}) == 1:
            return f"{x} won" if field[0][0] == x else f"{o} won"
        elif len({field[2][0], field[1][1], field[0][2]}) == 1:
            return f"{x} won" if field[2][0] == x else f"{o} won"
        elif len({field[0][2], field[1][1], field[2][0]}) == 1:
            return f"{x} won" if field[0][2] == x else f"{o} won"

    if no_more_moves:
        return "Game over"
    return "Next"
