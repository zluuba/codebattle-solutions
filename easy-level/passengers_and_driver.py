# A typical car can hold three passengers and one driver, allowing four people to travel somewhere.
# Given n number of people, calculate how many cars are needed to seat everyone comfortably.
#
# Examples:
# 0  == solution(0)
# 4  == solution(13)
# 1  == solution(4)
# 3  == solution(9)


def solution(people: int) -> int:
    seats = 4
    full_of_people_cars = people // seats
    seats_free_car = 0 if people % seats == 0 else 1
    return full_of_people_cars + seats_free_car
