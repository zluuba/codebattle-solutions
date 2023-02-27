# Implement a function that returns directories count (path includes directories or path directory itself).
#
# Examples:
# 1  == solution(["C:/Projects/something.txt","file.exe"])
# 0  == solution(["brain-games.exe","gendiff.sh","task-manager.rb"])
# 3  == solution(["C:/Users/JohnDoe/Music/Beethoven_5.mp3","/usr/bin","/var/www/myprojectt"])


from typing import List


def solution(filepaths: List[str]) -> int:
    directories = 0

    for path in filepaths:
        if '/' in path:
            directories += 1

    return directories
