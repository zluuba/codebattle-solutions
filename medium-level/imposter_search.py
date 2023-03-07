# Create a function that find imposters in array of players, each player has its own role.
# If no imposters were found, return ["there are no imposters here!"].
# If in array presented only imposters, return ["imposters are everywhere!"].
# In other cases return array of imposters names.
#
# Examples:
# ["Vasya","Jack"]  == solution([["Daniel","crewmate"],["Vasya","imposter"],["Jack","imposter"]])
# ["there are no imposters here!"]  == solution([["Harry","crewmate"]])
# ["imposters are everywhere!"]  == solution([["Jack","imposter"]])

from typing import List


def solution(players: List[List[str]]) -> List[str]:
    imposters = [player[0] for player in players if player[1] == 'imposter']

    if not imposters:
        return ["there are no imposters here!"]

    if len(imposters) == len(players):
        return ["imposters are everywhere!"]

    return imposters
