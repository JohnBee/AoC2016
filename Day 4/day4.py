
import re
import operator

input = ""
with open("input.txt","r") as f:
    input = f.readlines()

#strip input
for i in range(0,len(input)):
    input[i] = input[i].rstrip().lstrip()
    temp = input[i]
    input[i] = re.findall(r"([a-z]+)\-+?",temp)
    secIdCode = re.findall(r"([0-9]+)(\[[a-z]{5}\])", temp)[0]
    input[i] += secIdCode
    input[i][-1] = input[i][-1].replace("[","").replace("]","")

def genCode(wordList):
    letDict = {}
    pos = 0
    for i in range(0,len(wordList)):
        for j in range(0,len(wordList[i])):
            letter = wordList[i][j]
            if  letter in letDict.keys():
                letDict[letter][0] += 1
            else:
                letDict[letter] = [1,pos] #store first seen position with letter
            pos +=1
    #Turn in to touple for sorting
    letSorted = [(k, v) for k, v in letDict.iteritems()]
    #sort
    topFiveSorted = sorted(letSorted, key=lambda x: (-x[1][0],x[0]))[:5]
    return "".join([a for a,b in topFiveSorted])

count = 0
for i in input:
    code = genCode(i[:-2])
    print code,
    print i[-1]
    if code == i[-1]:
        count+=int(i[-2])
print count
