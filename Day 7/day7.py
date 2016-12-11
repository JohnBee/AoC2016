import re

input = ""
with open("input.txt","r") as f:
    input = f.readlines()

#strip input
for i in range(0,len(input)):
    input[i] = input[i].rstrip().lstrip().split()[0]
    #split in to text components
    splitText = re.findall(r"(([a-z]+)(\[[a-z]+\]))*?([a-z]+)",input[i])
    splitText = [a[3] for a in splitText]
    input[i] = splitText
    # Even index out of bracket,
    # Odd index inside brackets

def ABBA(word):
    if word[0] == word[3] and word[1] == word[2] and word[1] != word[3]:
        return True
    return False

def ABBAcheck(word):
    for i in range(0,len(word)-3):
        # sliding window
        if ABBA(word[i:i+4]):
            return True
    return False

count = 0
def checkInput(i):
    passed = False
    for words in range(0,len(i),2):
        # check outside brackets
        if ABBAcheck(i[words]) == True:
            passed = True
    if passed == True:
        for words in range(1,len(i),2):
            # check inside brackets
            if ABBAcheck(i[words]) == True:
                return False
    else:
        return False
    return passed

for i in input:
     if checkInput(i):
         count +=1
print count
