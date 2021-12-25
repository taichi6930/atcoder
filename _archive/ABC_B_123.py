import math

minMod = 10
minModNum = 0
numList = []
for i in range(0, 5):
    numList.append(int(input()))
    if ((numList[i] % 10 != 0) & (numList[i] % 10 < minMod)):
        minMod = numList[i] % 10
        minModNum = i

sum = 0
for i in range(0, 5):
    if i != minModNum:
        sum += int(math.ceil(numList[i]/10)*10)
    else:
        sum += numList[i]
print(sum)
