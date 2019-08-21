X, Y, Z, K = map(int, input().split())
AiList = list(map(int, input().split()))
AiList.sort(reverse=True)
BiList = list(map(int, input().split()))
BiList.sort(reverse=True)
CiList = list(map(int, input().split()))
CiList.sort(reverse=True)

resultList = []
for x in range(0, X):
    for y in range(0, Y):
        for z in range(0, Z):
            resultList.append(AiList[x] + BiList[y] + CiList[z])
resultList.sort(reverse=True)
for i in range(0, K):
    print(resultList[i])
