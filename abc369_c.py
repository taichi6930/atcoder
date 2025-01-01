n = int(input())
A = list(map(int, input().split()))

ansDict = {}

for i in range(n - 2):
    if A[i + 1] - A[i] == A[i + 2] - A[i + 1]:
        ansDict[i] = i + 2

for i in range(n - 1):
    print(n - i - 1)


# 2次元配列を作る
# 2次元配列の中身を表示する
A = [[0] * n for i in range(n)]
