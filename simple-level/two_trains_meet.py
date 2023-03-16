# Compute how long after their deparature two trains will meet.
# Assume that the trains travel between two points, along a single section of track, going in opposite directions.
# The function should consume the trains' speeds and the starting distance between the trains.

# Examples:
# 1.0  == solution(50, 50, 100)
# 2.0  == solution(30, 40, 140)
# 3.0  == solution(70, 50, 360)


def solution(v1: int, v2: int, distance: int) -> float:
    return distance / (v1 + v2)
