n, k, q = map(int, input().split())
nList = [0] * n
for _ in range(q):
    nList[int(input()) - 1] += 1
for j in range(n):
    print("Yes" if k + nList[j] - q > 0 else "No")
