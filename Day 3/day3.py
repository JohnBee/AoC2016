input = ""
with open("input.txt","r") as f:
    input = f.readlines()

#strip input
for i in range(0,len(input)):
    input[i] = input[i].rstrip().lstrip().split()
    input[i] = [int(a) for a in input[i]]

count = 0
for i in input:
    if i[0] + i[1] > i[2] and i[0] + i[2] > i[1] and i[1] + i[2] > i[0]:
        count +=1
print count
