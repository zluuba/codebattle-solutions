# Calculate the Levenshtein distance.
#
# Examples:
# 3  == solution("kitten", "sitting")
# 1  == solution("clojure", "closure")
# 2  == solution("xyx", "xyyyx")
# 6  == solution("", "123456")


def solution(s1: str, s2: str) -> int:
    length_s1, length_s2 = len(s1), len(s2)
    if length_s1 > length_s2:
        s1, s2 = s2, s1
        length_s1, length_s2 = length_s2, length_s1

    curr_row = range(length_s1 + 1)
    for i in range(1, length_s2 + 1):
        prev_row, curr_row = curr_row, [i] + [0] * length_s1
        for j in range(1, length_s1 + 1):
            add, delete, update = prev_row[j] + 1, curr_row[j - 1] + 1, prev_row[j - 1]
            if s1[j - 1] != s2[i - 1]:
                update += 1
            curr_row[j] = min(add, delete, update)

    return curr_row[length_s1]
