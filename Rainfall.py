#create a list and recieve data from user
rainfall = []
print('This program will do things with the rainfall for the year')
print('----------------------------------------------------------')
myData = input('What is the monthly rainfall for the past 12 months e.g. 12,23,12,5: ')
rainfall = myData.split(',')
print(rainfall)

rainfall = int(myData)
sortFall = rainfall.sort()
print(sortFall)

for i in range(len(rainfall)):
    rainfall[i] = int(rainfall[i])

total = 0
for x in rainfall:
    total += x

maxFall = max(rainfall)
minFall = min(rainfall)
averageFall = total/len(rainfall)

print('The highest rainfall was {0} \n'
    'The lowest rainfall was {1} \n'
    'The average rainfall was {2} \n'.format(maxFall,minFall,averageFall))
