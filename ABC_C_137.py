N = int(input())
cnt = 0

sList = []

for n in range(0, N):
    string = list(input())
    sList.append(string)
    sList[n].sort()
    print(sList[n])

for i in range(0, N - 1):
    for j in range(i + 1, N):
        if sList[i] == sList[j]:
            cnt += 1
print(cnt)
