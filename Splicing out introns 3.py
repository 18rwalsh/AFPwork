dnaSeq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

#find exon 1
exon1 = dnaSeq[0:63]

#find intron
intron = dnaSeq[63:90]

#find exon 2
exon2 = dnaSeq[90:]

#print out coding and non coding sections
print('Original sequence: {0}'.format(dnaSeq))
print("Coding DNA: {0}\nNon Coding DNA: {1}\nCoding DNA: {2}".format(exon1, intron.lower(),exon2))
