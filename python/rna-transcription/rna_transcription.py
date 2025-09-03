def to_rna(dna_strand):
    rna_strand = ""

    for nucleotide in dna_strand:
        if nucleotide == "" and len(dna_strand) == 1:
            return ""
        
        if nucleotide == "G":
            rna_strand += "C"

        if nucleotide == "C":
            rna_strand += "G"

        if nucleotide == "T":
            rna_strand += "A"

        if nucleotide == "A":
            rna_strand += "U"

    return rna_strand

print(to_rna("ACGTGGTCTTAA"))