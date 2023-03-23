# Write a function that gets a string number and a fret of a 6-string guitar in 'standard tuning'
# and return the corresponding note. For this challenge we use a 24 fret model.
# The notes are: C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, G#/Ab, A, A#/Bb, B

# Examples:
# "A"  == solution(3, 2)
# "A#"  == solution(1, 6)
# "G"  == solution(3, 0)
# "F#"  == solution(2, 19)


def solution(str: int, fret: int) -> str:
    tun = ['E', 'B', 'G', 'D', 'A', 'E']
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    t = tun[str - 1]
    ind = notes.index(t) + fret

    if ind >= len(notes):
        ind = ind % len(notes)

    return notes[ind]
