n = int(input())
numList = [True for _ in range(2 * n + 1)]

numMin = 1


for i in range(n + 1):
    for j in range(2 * n + 2):
        if numList[numMin - 1]:
            print(numMin)
            numList[numMin - 1] = False
            numMin += 1
            break
        numMin += 1

    q = int(input())
    if q == 0:
        break
    numList[q - 1] = False
