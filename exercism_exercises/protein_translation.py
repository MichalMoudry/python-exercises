"""
Protein translation exercise module.
"""

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
    print(chunk_iterable(strand, 3))
    pass

if __name__ == "__main__":
    print(proteins("AUGUUUUCU"))
