# A farmer is asking you to tell him how many legs can be counted among all his animals.
# The farmer breeds three species: chickens = 2 legs cows = 4 legs pigs = 4 legs The farmer has counted his animals
# and he gives you a subtotal for each species.
# You have to implement a function that returns the total number of legs of all the animals.

# Examples:
# 36  == solution(2, 3, 5)
# 22  == solution(1, 2, 3)
# 50  == solution(5, 2, 8)


def solution(chickens: int, cows: int, pigs: int) -> int:
    chickens_legs = 2
    cows_and_pigs_legs = 4

    return chickens * chickens_legs + (cows + pigs) * cows_and_pigs_legs
