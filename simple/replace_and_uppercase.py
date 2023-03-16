# You are given a string of words. You need replace _ symbols with spaces and capitalize every word in a string.
#
# Examples:
# "Learn Clojure Be Happy"  == solution("learn_clojure_be_happy")
# "Learn Ruby Win Tournaments"  == solution("learn_ruby_win_tournaments")


def solution(sentence: str) -> str:
    sentence_lst = sentence.split('_')
    result = ' '.join(sentence_lst)
    return result.title()
