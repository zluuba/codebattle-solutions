# Return a new hash map with elements of the given array as keys, and the given default value as values for those keys.
#
# Examples:
# {"draft":0,"completed":0}  == solution(["draft","completed"], 0)
# {"one":4,"two":4}  == solution(["one","two"], 4)

from typing import List, Dict


def solution(words: List[str], num: int) -> Dict[str, int]:
    return {word: num for word in words}
