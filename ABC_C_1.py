rate = 0
N, K = map(int, input().split())
coderList = list(map(int, input().split()))
coderList.sort(reverse=True)
for i in range(0, K):
    rate = (rate + coderList[K - i - 1]) / 2
print(rate)
