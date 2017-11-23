dnaSeq = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

#seperate the letters seperately
seqReplace1 = dnaSeq.replace('A', 'c')
seqReplace2 = dnaSeq.replace('C', 'a')
seqReplace3 = dnaSeq.replace('T', 'g')
seqReplace4 = dnaSeq.replace('G', 't')

#replaces C with a in seqReplace1, now has lower case c and a in it
newSeq = seqReplace1.replace('C', 'a')

#replaces T with g in newSeq, now has lower case c, a and g
newSeq1 = newSeq.replace('T','g')

#replaces T with g in newSeq1, now has lower case c, a, g and t
newSeq2 = newSeq1.replace('G', 't')

#prints the original sequence
print('Original Sequence:', dnaSeq)

#prints complement sequence in upper case
seqUpper = newSeq2.upper()
print('Complement Sequence:', seqUpper)