# You are given a string of words. You need to find the word Nemo, and return a string like
# this: "I found Nemo at [the order of the word you find nemo]!".
# If you can't find Nemo, return "I can't find Nemo :(".
#
# Examples:
# "I can't find Nemo :("  == solution("Hello world")
# "I found Nemo at 2!"  == solution("Hi Nemo")
# "I found Nemo at 1!"  == solution("Nemo James Nemo")
# "I found Nemo at 1!"  == solution("Nemo is me")


def solution(sentence: str) -> str:
    looking_for = 'Nemo'
    sentence = sentence.split()

    for ind, word in enumerate(sentence, 1):
        if word == looking_for:
            return f'I found Nemo at {ind}!'

    return "I can't find Nemo :("
