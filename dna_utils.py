# dna_utils.py

def clean_sequence(seq: str) -> str:
    """Clean input DNA sequence by removing non-ATGC characters."""
    return ''.join([s for s in seq.upper() if s in ['A', 'T', 'G', 'C']])

def get_base_counts(seq: str) -> dict:
    """Return the count of each base in the DNA sequence."""
    return {
        'A': seq.count('A'),
        'T': seq.count('T'),
        'G': seq.count('G'),
        'C': seq.count('C')
    }

def gc_content(seq: str) -> float:
    """Calculate GC content percentage."""
    gc = seq.count('G') + seq.count('C')
    return round((gc / len(seq)) * 100, 2) if seq else 0
