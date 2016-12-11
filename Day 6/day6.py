input = ""
with open("input.txt","r") as f:
    input = f.readlines()

#strip input
for i in range(0,len(input)):
    input[i] = input[i].rstrip().lstrip().split()[0]

letCount = {}
for letI in range(0,len(input[0])):
    letCount[letI] = {}
    for word in input:
        let = word[letI]
        if let in letCount[letI].keys():
             letCount[letI][let] +=1
        else:
            letCount[letI][let] = 1
            
#convert to tuples and sort
for key in letCount.keys():
    letCount[key] = [(k, v) for k, v in letCount[key].iteritems()]
    letCount[key] = sorted(letCount[key], key=lambda x: x[1],reverse=True)
    print letCount[key][0][0],
print ""
