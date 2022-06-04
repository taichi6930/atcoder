S = list(input())[::-1]
lenS = len(S)
numList = [[i for i in range(10)] for _ in range(lenS)]

for i in range(len(S) - 1):
    for j in range(10):
        numList[i + 1][j] = (numList[i][j] * 10) % 13

dp = [[0 for _ in range(10)] for _ in range(lenS)]
