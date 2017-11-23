#DNA Sequence
dnaSeq = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'

#finding the 2 exons
exon1 = dnaSeq[0:63]
exon2 = dnaSeq[91:]

#printing both
print('Original Sequence: {0}'.format(dnaSeq))
print('Coding Exon 1: {0}\nCoding Exon 2: {1}'.format(exon1, exon2))