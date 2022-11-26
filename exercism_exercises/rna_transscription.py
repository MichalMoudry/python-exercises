"""
RNA transcription exercise module.
"""

def to_rna(dna_strand: str):
    if dna_strand == "": return ""
    result: list[str] = []
    for item in dna_strand:
        if item == "G":
            result.append("C")
        elif item == "C":
            result.append("G")
        elif item == "T":
            result.append("A")
        else:
            result.append("U")
    return "".join(result)

if __name__ == "__main__":
    print(to_rna(""))
    print("G =>", to_rna("G"), "(Expected: C)")
    print("C =>", to_rna("C"), "(Expected: G)")
    print("A =>", to_rna("A"), "(Expected: U)")
    print("ACGTGGTCTTAA =>", to_rna("ACGTGGTCTTAA"), "(Expected: UGCACCAGAAUU)")
