# The Baudot code or International Teleprinter Code was invented by Emile Baudot in 1870.
# It was used for teleprinter messages instead of the morse code. Baudot uses five bits per character,
# thus allowing up to 32 distinct characters. As a technique used to extend this limitation,
# the code uses up-shift and down-shift modes as is used on a typewriter.
# In the Baudot code, each five bits transmitted must be interpreted according to whether they are up-shifted
# (figures) or down-shifted (letters).
# For example, the bit pattern 11111 represents up-shift and the bit pattern 11011 represents down-shift characters.
# All characters transmitted after the sequence 11111 but before the shifted sequence 11011 are treated as up-shift
# characters.
# All characters transmitted after the sequence 11011 are treated as down-shift characters until
# the pattern 11111 is recognized.
# Code Letter Figure .o.o. R 4 .o.oo J Not allocated .ooo. C : oo.o. G Not allocated .o..o D Not allocated
# .oooo K ( .oo.. N , ...oo A - ..... BLANK oo.oo Figures(F) SHift ..oo. I 8 oo... O 9 oooo. V = o..o. L )
# .oo.o F Not allocated ....o E 3 ..ooo U 7 oo..o B ? ..o.. SPACE ooooo Letters(L) shift ooo.. M : o..oo W 2
# o.oo. P 0 ..o.o S , ooo.o X / o...o Z + o.ooo Q 1 o.o.. H Not allocated o.o.o Y 6 o.... T 5


def solution(code: str) -> str:
    keys = {
        '.o.o.': ('R', '4'), '.o.oo': ('J', ''), '.ooo.': ('C', ':'), 'oo.o.': ('G', ''),
        '.o..o': ('D', ''), '.oooo': ('K', '('), '.oo..': ('N', ','), '...oo': ('A', '-'),
        '..oo.': ('I', '8'), 'oo...': ('O', '9'), 'o.o.o': ('Y', '6'), 'o....': ('T', '5'),
        'oooo.': ('V', '='), 'o..o.': ('L', ')'), '.oo.o': ('F', ''), '....o': ('E', '3'),
        'ooo..': ('M', ':'), 'o..oo': ('W', '2'), 'o.oo.': ('P', '0'), '..o.o': ('S', ','),
        'ooo.o': ('X', '/'), 'o...o': ('Z', '+'), 'o.ooo': ('Q', '1'), 'o.o..': ('H', ''),
        '..ooo': ('U', '7'), 'oo..o': ('B', '?'), '..o..': (' ', ' '),
        '.....': (' ', ' ') if ' ' in code else ('', ''),
        'oo.oo': 'figures', 'ooooo': 'letters',
    }

    chunks = [code[i:i + 5] for i in range(0, len(code), 5)]
    flag = 'letters'

    result = ''
    for chunk in chunks:
        if chunk not in keys or len(chunk) != 5:
            continue

        key = keys[chunk]
        if key in {'figures', 'letters'}:
            flag = key
            continue
        result += key[0] if flag == 'letters' else key[1]

    return result
