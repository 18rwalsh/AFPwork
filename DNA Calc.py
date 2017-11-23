#sequence needed to count
#dnaSequence = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

#Let the user know what the program does
print('This Program will display the GC content of a DNA sequence')
dnaSequence = input('Enter your DNA sequence ')

#change the input to uppercase
dnaSequence = dnaSequence.upper()

#count the number of C in sequence
numC = dnaSequence.count('C')
print(numC)

#count the number of G in sequence
numG = dnaSequence.count('G')
print(numG)

#find the length of the sequence
sequenceLength = len(dnaSequence)
print(sequenceLength)

#calculate the %
totalPercent = (numC+numG)/sequenceLength*100
print(round(totalPercent, 2))
print('The GC content of the sequence is {0:.2f}%'.format(totalPercent))