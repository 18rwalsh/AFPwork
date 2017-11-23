seq = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'

#find the GAATTC and count the length
frag1 = seq.find('GAATTC') + 1

#find lenght of second frag
frag2 = len(seq) - frag1

#print lengths
print('The length of the first fragment is ' + str(frag1))
print('The length of the second fragment is ' + str(frag2))
