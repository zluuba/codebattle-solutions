# Luke Skywalker has family and friends. Help him remind them who is who.
# Given a string with a name, return the relation of that person to Luke.
# Person | Relation
# Darth Vader | father, Leia | sister, Han | brother in law, R2D2 | droid
#
# Examples:
# "Luke, I am your father."  == solution("Darth Vader")
# "Luke, I am your sister."  == solution("Leia")
# "Luke, I am your droid."  == solution("R2D2")
# "Luke, I am your brother in law."  == solution("Han")


def solution(person: str) -> str:
    relations = {
        'Darth Vader': 'father',
        'Leia': 'sister',
        'R2D2': 'droid',
        'Han': 'brother in law'
    }

    return f'Luke, I am your {relations[person]}.'
