# Create a function that inverts the RGB values of a given array.
#
# Examples:
# [0,0,0]  == solution([255,255,255])
# [255,255,255]  == solution([0,0,0])
# [90,85,34]  == solution([165,170,221])


from typing import List


def solution(colours: List[int]) -> List[int]:
    max_color_val = 255
    invert_colours = [max_color_val - color for color in colours]
    return invert_colours
