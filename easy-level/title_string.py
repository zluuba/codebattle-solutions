# Check if a string title is a title string or not. A title string is one which has all the words in the string
# start with an upper case letter.
#
# Examples:
# false  == solution("There are three types of zeros in JS!")
# true  == solution("Learn Clojure Be Happy!")
# false  == solution("Learn Ruby win tournaments?!")
# true  == solution("Simple Title.")

def solution(title: str) -> bool:
    return title == title.title()
