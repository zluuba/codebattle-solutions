# Given an array that contains the following information about a student: student-name - the student's name/surname
# and discipline - the subject that student is studying. Return the array of names formatted
# by the following rule Harry Potter -> harry-potter.

# Examples:
# ["harry-potter"]  == solution([{"student-name": "Harry Potter" ,"discipline": "Magic"}])
# ["luke-skywalker" ,"hermione-granger", "walter-white"]  == solution(
# [{"student-name": "Luke Skywalker", "discipline": "Jedi"},
# {"student-name": "Hermione Granger", "discipline": "Magic"},
# {"student-name": "Walter White", "discipline": "Chemistry"}]
# )


from typing import List, Dict


def solution(students: List[Dict[str, str]]) -> List[str]:
    result = []
    for student in students:
        name = student['student-name']
        name = name.lower().replace(' ', '-')
        result.append(name)

    return result
