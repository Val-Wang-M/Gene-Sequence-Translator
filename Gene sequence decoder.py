gene = str(input("Enter gene sequence: "))
lst = list(gene)
mRNA = []
abnormal = 0
i = 0
aminoAcid = []
for base in lst:
    if base == "A" or base == "a":
        mRNA.append("U")
    elif base == "T" or base == "t":
        mRNA.append("A")
    elif base == "G" or base == "g":
        mRNA.append("C")
    elif base == "C" or base == "c":
        mRNA.append("G")
    else:
        abnormal += 1
mRNAString = "".join(mRNA)
if abnormal == 0:
    print("mRNA strand: ", mRNAString)
    mRNASequence = [''.join(mRNA[i:i+3]) for i in range(0, len(lst), 3)]
    #print(result)  # Output: ['AUG', 'UGA']
    for codon in mRNASequence:
        if codon == 'UUU' or codon == 'UUC':
            aminoAcid.append("Phe ")
        elif codon == "UUA" or codon == "UUG" or codon == "CUU" or codon == "CUC" or codon == "CUA" or codon == "CUG":
            aminoAcid.append("Leu ")
        elif codon == "AUU" or codon == "AUC" or codon == "AUA":
            aminoAcid.append("Ile ")
        elif codon == "AUG":
            aminoAcid.append("Met ")
        elif codon == "GUU" or codon == "GUA" or codon == "GUC" or codon == "GUG":
            aminoAcid.append("Val ")
        elif codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG" or codon == "AGU" or codon == "AGC":
            aminoAcid.append("Ser ")
        elif codon == "CCU" or codon == "CCC" or codon == "CCG" or codon == "CCA":
            aminoAcid.append("Pro ")
        elif codon == "ACU" or codon == "ACC" or codon == "ACA" or codon == "ACG":
            aminoAcid.append("Thr ")
        elif codon == "GCU" or codon == "GCC" or codon == "GCA" or codon == "GCG":
            aminoAcid.append("Ala ")
        elif codon == "UAU" or codon == "UAC":
            aminoAcid.append("Tyr ")
        elif codon == "CAU" or codon == "CAC":
            aminoAcid.append("His ")
        elif codon == "CAA" or codon == "CAG":
            aminoAcid.append("Gln ")
        elif codon == "AAU" or codon == "AAC":
            aminoAcid.append("Asn ")
        elif codon == "AAA" or codon == "AAG":
            aminoAcid.append("Lys ")
        elif codon == "GAU" or codon == "GAC":
            aminoAcid.append("Asp ")
        elif codon == "GAA" or codon == "GAG":
            aminoAcid.append("Glu ")
        elif codon == "UGU" or codon == "UGC":
            aminoAcid.append("Cys ")
        elif codon == "UGG":
            aminoAcid.append("Trp ")
        elif codon == "GGU" or codon == "GGC" or codon == "GGA" or codon == "GGG":
            aminoAcid.append("Gly ")
        elif codon == "CGU" or codon == "CGC" or codon == "CGA" or codon == "CGG" or codon == "AGA" or codon == "AGG":
            aminoAcid.append("Ser ")
        else:
            break
            
else:
    print("Alien gene detected.")
#print(mRNAString)
print("- ".join(aminoAcid))