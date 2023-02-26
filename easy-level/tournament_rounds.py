# Codebattle players are paired up to play one round of games. There is always one winner from each pair.
# New rounds are created until one pair of players remains.
# For example, for 8 players there will be 3 rounds: 1/4 finals, 1/2 finals and final.
# Create a function that takes the number of participants and returns the number of rounds.

# Examples:
# 1  == solution(2)
# 4  == solution(16)
# 5  == solution(32)
# 3  == solution(8)


def solution(participants: int) -> int:
    rounds = 0
    while participants > 1:
        participants = participants // 2
        rounds += 1

    return rounds
