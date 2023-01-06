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
    "Tryptophan": ("UGG",)
}

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
    print(inpt)
    for protein in PROTEINS:
        print("---", protein, PROTEINS[protein])
        evl = [prot in inpt for prot in PROTEINS[protein]]
        print(evl, all(evl))
    pass

if __name__ == "__main__":
    print(proteins("AUGUUUUCUUAAAUG"))
