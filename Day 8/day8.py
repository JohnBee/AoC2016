import copy
screen = [[" " for x in range(50)] for y in range(6)]
input = ""
with open("input.txt","r") as f:
    input = f.readlines()

#strip input
for i in range(0,len(input)):
    input[i] = input[i].rstrip().lstrip().split()

    if input[i][0] == "rect":
        input[i][1] = [int(a) for a in input[i][1].split("x")]
    if input[i][0] == "rotate":
        input[i][2] = int(input[i][2][2:])
        input[i][3] = int(input[i][-1:][0])
        input[i] = input[i][:4]
    #print input[i]
#parse input
def printScreen(screen):
    out = ""
    for a in screen:
        out += "".join(a)+"\n"
    print out

def newPosRow(start,shift):
    return ((start+shift % 50) + 50) % 50

def newPosColumn(start,shift):
    return ((start+shift % 6) + 6) % 6

def rectAB(screen, A,B):
    for y in range(0,B):
        for x in range(0,A):
            screen[y][x] = "#"

def rotRow(screen, A,B):
    copyScreen = copy.deepcopy(screen)
    for x in range(0,50):
        screen[A][newPosRow(x,B)] = copyScreen[A][x]

def rotCol(screen,A,B):
    copyScreen = copy.deepcopy(screen)
    for x in range(0,6):
        screen[newPosColumn(x,B)][A] = copyScreen[x][A]

#do instructons
for i in input:
    if i[0] == "rect":
        rectAB(screen, i[1][0],i[1][1])
    if i[0] == "rotate":
        if i[1] == "row":
            rotRow(screen, i[2],i[3])
        if i[1] == "column":
            rotCol(screen, i[2],i[3])

printScreen(screen)
count = 0
for y in screen:
    for x in y:
        if x == "#":
            count +=1
print count
