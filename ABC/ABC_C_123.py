import math

N = int(input())
minNum = int(input())
for i in range(1, 5):
    inputNum = int(input())
    if minNum > inputNum:
        minNum = inputNum
print(math.ceil(N/minNum) + 4)
