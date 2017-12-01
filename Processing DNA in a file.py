#open DNA text file
file = open('ex3-1_input.txt')

#open file data is being put in
newSeq = open('New_code.txt', 'w')

#find length of data
for line in file:
    dnaLen = len(line)
    trimmedLine = line[14:dnaLen]
    print(trimmedLine)
    print('Trimmed line is:',len(trimmedLine),'values long.')
    newSeq.write(trimmedLine)
    newSeq.write('\n')
file.close()
newSeq.close()
