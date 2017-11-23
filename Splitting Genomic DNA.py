dnaSeq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
myFile1 = open('CodingDNA.txt', 'w')
myFile2 = open('NonCodingDNA.txt', 'w')

#find exon 1
exon1 = dnaSeq[0:63]

#find intron
intron = dnaSeq[63:90]

#find exon 2
exon2 = dnaSeq[90:]

myFile1.write("Coding DNA: {0}\nCoding DNA: {1}".format(exon1, exon2))
myFile2.write('Non Coding DNA: {0}'.format(intron))