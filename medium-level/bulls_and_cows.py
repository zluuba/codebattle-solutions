# On a sheet of paper, the players each write a 4-digit secret number. The digits must be all different.
# Then, in turn, the players try to guess their opponent's number who gives the number of matches.
# If the matching digits are in their right positions, they are bulls, if in different positions, they are cows.
# Write the function that calculates bulls and cows.

# Examples:
# [1,2]  == solution(4271, 1234)
# [0,1]  == solution(4271, 5682)
# [4,0]  == solution(4271, 4271)
# [1,1]  == solution(4182, 4273)

from typing import List


def solution(secret: int, guess: int) -> List[int]:
    secret, guess = str(secret), str(guess)

    bulls, cows = 0, 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1

    return [bulls, cows]
