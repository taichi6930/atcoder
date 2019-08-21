N = int(input())
numList = [8, 4, 2, 1]
ansList = []

for num in numList:
    if N // num == 1:
        ansList.append(num)
        N -= num

print(len(ansList))
for ans in ansList:
    print(ans)
