# In a given word array, replace the vowels in each word with their indexes.
# The indexes are numbered starting from zero.
#
# Examples:
# ["cl2j4r6","p1th4n","0l2x4r","j1v3scr7pt"]  == solution(["clojure","python","elixir","javascript"])
# ["s1l3ngw7rd","w1ws4l6ngw10rd","w1ws4m6chl10ngw14rd"]  == solution(["solongword","wowsolongword","wowsomuchlongword"])
# ["wh23456t","0b234567t","th2345t?"]  == solution(["whaaaaat","abooouuut","thaaaat?"])


from typing import List


def solution(words: List[str]) -> List[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    result = []

    for word in words:
        new_word = ''
        for ind, char in enumerate(word):
            if char in vowels:
                char = str(ind)
            new_word += char
        result.append(new_word)

    return result
