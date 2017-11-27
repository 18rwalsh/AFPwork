#opening and preparing the file to be read and manipulated
dnaSeq = open('/Users/xRazerSwiftx/Desktop/genomic_dna.txt')
myDna = dnaSeq.read().strip('\n')

#creating the files
myFile1 = open('CodingDNA.txt', 'w')
myFile2 = open('NonCodingDNA.txt', 'w')

#find exon 1
exon1 = myDna[0:63]

#find intron
intron = myDna[63:90]

#find exon 2
exon2 = myDna[90:]

#writing the str to the files
myFile1.write("Coding DNA: {0}\nCoding DNA: {1}".format(exon1, exon2))
myFile2.write('Non Coding DNA: {0}'.format(intron))

myFile1.close()
myFile2.close()