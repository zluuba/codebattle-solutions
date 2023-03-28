# Find all the anagrams in a vector of words. Your function should return a vector of vectors,
# where each sub-vector is a group of words which are anagrams of each other.
# Words without any anagrams should not be included in the result.
# If there is no anagram, return subvector with string "anagrams not found!"
#
# Examples:
# [["veer","ever"],["lake","kale"],["item","mite"]]  == solution(["veer","lake","item","kale","mite","ever","rev"])
# [["meat","team","mate","mate"]]  == solution(["meat","mat","team","mate","eat","mate"])
# [["anagrams not found!"]]  == solution(["there","is","no","anagrams","foo","bar"])
# [["guohc","guohc","cough"],["osls","osls"],["nitwer","trnwie"],["distribution","oriintdusbti"],["water","water"],
# ["nuaegalg","gelugaan"]]  == solution(["guohc","guohc","cough","morning","adigrne","osls","sneeze","knowledge",
# "nitwer","distribution","water","ewvi","event","oriintdusbti","trnwie","water","nuaegalg","osls","gelugaan","question"])

from typing import List


def solution(words: List[str]) -> List[List[str]]:
    anagrams = []
    anagrams_idxs = []

    for i in range(len(words)):
        temp = []
        for j in range(i + 1, len(words)):
            curr1, curr2 = words[i], words[j]
            if sorted(curr1) == sorted(curr2):
                if i not in anagrams_idxs:
                    temp.append(curr1)
                    anagrams_idxs.append(i)
                if j not in anagrams_idxs:
                    temp.append(curr2)
                    anagrams_idxs.append(j)
        if temp:
            anagrams.append(temp)

    return anagrams if anagrams else [["anagrams not found!"]]
