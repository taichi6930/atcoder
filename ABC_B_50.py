N = int(input())
TList = list(map(int, input().split()))

M = int(input())

for m in range(0, M):
    P, X = map(int, input().split())
    print(sum(TList) - TList[P - 1] + X)
