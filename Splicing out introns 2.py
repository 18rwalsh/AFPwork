#DNA Sequence
dnaSeq = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'

#finding exons
exon1 = dnaSeq[0:63]
exon2 = dnaSeq[91:]

#finding lenghts
exonLen = len(exon1 + exon2)
seqLen = len(dnaSeq)

#printing and working out percentage
print('The percentage of DNA coding is {0:.2f}%'.format(exonLen/seqLen*100))

