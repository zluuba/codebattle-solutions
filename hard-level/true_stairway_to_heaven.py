# N dicks randomly spread out of M stairs, there can be as many dicks as you want on one step.
# We gotta go down these stairs. Every time you step on a stair-step with dicks, the infame number increases by
# the number of dicks. You can go down one or two steps at a time.
# Write a function to descend the stairs minimizing the infame number.
# The function receives an array with the number of dicks on each step and returns the minimized infame number.
# Powered by Eugene Zaytsev.

# Examples:
# 0  == solution([0,1,0,1])
# 0  == solution([1,0,1,0,1])
# 6  == solution([1,0,3,5,10,0,11,1])
# 17  == solution([0,11,6,8,1,4,10,9])
# 30  == solution([9,11,1,5,6,6,5,4,9,12])

from typing import List


def solution(arr: List[int]) -> int:
    step1 = arr[0]
    step2 = arr[1]

    for i in range(2, len(arr)):
        step1, step2 = step2, min(step1, step2) + arr[i]

    return min(step1, step2)
