# Implement a function that returns the filename with extension from a given path.
#
# Examples:
# "something.txt"  == solution("C:/Projects/tests/texts/something.txt")
# "brain-games.exe"  == solution("C:/brain-games.exe")
# "Beethoven_5.mp3"  == solution("C:/Users/JohnDoe/Music/Beethoven_5.mp3")


def solution(filepath: str) -> str:
    *dirs, file = filepath.split('/')
    return file
