n, k = map(int, input().split())
abList = []
for i in range(n):
    a, b = map(int, input().split())
    abList.extend([a] * b)
print(abList[k-1])
