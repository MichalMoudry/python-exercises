"""
Protein translation exercise module.
"""

PROTEINS = {
    "Methionine": ("AUG",),
    "Phenylalanine": ("UUU", "UUC"),
    "Leucine": ("UUA", "UUG"),
    "Serine": ("UCU", "UCC", "UCA", "UCG"),
    "Tyrosine": ("UAU", "UAC"),
    "Cysteine": ("UGU", "UGC"),
    "Tryptophan": ("UGG",),
    "STOP": ("UAA", "UAG", "UGA")
}

PROTEIN_KEYS = list(PROTEINS.keys())

def chunk_iterable(iterable, chunk_size: int):
    """
    Function for chunking an iterable object.
    """
    result = []
    for item in enumerate(iterable):
        if item[0] % chunk_size == 0:
            result.append(iterable[item[0]:item[0]+chunk_size])
    return result

def proteins(strand: str):
    inpt = chunk_iterable(strand, 3)
    protein_index = 0
    result: list[str] = []
    for protein in inpt:
        protein_index = [item[0] for item in enumerate(PROTEINS.values()) if protein in item[1]][0]
        if PROTEIN_KEYS[protein_index] == "STOP":
            break
        result.append(PROTEIN_KEYS[protein_index])
    return result

if __name__ == "__main__":
    print(proteins("AUGUUUUCUUAAAUG"))
