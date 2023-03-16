# Create a function that takes a whole number as input and returns the shape with
# that number's amount of sides. Check examples below.
#
# Examples:
# "circle"  == solution(1)
# "semi-circle"  == solution(2)
# "triangle"  == solution(3)
# "square"  == solution(4)
# "pentagon"  == solution(5)
# "hexagon"  == solution(6)
# "heptagon"  == solution(7)
# "octagon"  == solution(8)
# "nonagon"  == solution(9)
# "decagon"  == solution(10)


def solution(sides: int) -> str:
    shapes = {
        1: 'circle', 2: 'semi-circle', 3: 'triangle',
        4: 'square', 5: 'pentagon', 6: 'hexagon',
        7: 'heptagon', 8: 'octagon', 9: 'nonagon',
        10: 'decagon'
    }

    return shapes[sides]
