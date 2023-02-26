# Given a DNA strand, return its RNA complement. Both DNA and RNA strands are a sequence of nucleotides.
# DNA's nucleotides are adenine (A), cytosine (C), guanine (G) and thymidine (T).
# RNA's nucleotides are adenine (A), cytosine (C), guanine (G) and uracil (U).
# The transcribed RNA strand of a DNA strand is formed by replacing each nucleotide with its
# complement: G -> C, C -> G, T -> A, A -> U.

# Examples:
# "UGCACCAGAAUU"  == solution("ACGTGGTCTTAA")
# "G"  == solution("C")
# "C"  == solution("G")
# "U"  == solution("A")


def solution(dna: str) -> str:
    dna_to_rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

    rna = ''
    for nucl in dna:
        rna += dna_to_rna[nucl]

    return rna
