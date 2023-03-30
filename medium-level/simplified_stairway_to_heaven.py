# N dicks randomly spread out of M stairs, there can be as many dicks as you want on one step.
# We gotta go down these stairs. Every time you step on a stair-step with dicks, the infame number increases
# by the number of dicks. You can go down one or two steps at a time
# (You can`t lookup infame number farther than two steps away from you!).
# Write a function to descend the stairs minimizing the infame number (function must find local minimun at each step!).
# The function receives an array with the number of dicks on each step and returns the minimized infame number.
# Powered by Eugene Zaytsev.

# Examples:
# 0  == solution([0,1,0,1])
# 0  == solution([1,0,1,0,1])
# 9  == solution([1,0,3,5,10,0,11,1])
# 20  == solution([0,11,6,8,1,4,10,9])
# 34  == solution([9,11,1,5,6,6,5,4,9,12])

from typing import List


def solution(arr: List[int]) -> int:
    i = 0 if arr[0] < arr[1] else 1
    result = arr[i]

    while True:
        if i + 2 >= len(arr):
            return result

        if arr[i + 1] < arr[i + 2]:
            result += arr[i + 1]
            i += 1
        else:
            result += arr[i + 2]
            i += 2
