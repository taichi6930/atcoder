aList = list(map(int, input().split()))
ansList = []

for i in range(0, 3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            ansList.append(aList[i] + aList[j] + aList[k])

print(sorted(list(set(ansList)), reverse=True)[2])
