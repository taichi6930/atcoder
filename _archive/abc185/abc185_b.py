n, m, t = map(int, input().split())
maxN = n
abList = [list(map(int, input().split())) for _ in range(m)] + [[t, 0]]
n -= abList[0][0]
if n <= 0:
    print("No")
    exit()
for i in range(m):
    n = min(maxN, n + (abList[i][1] - abList[i][0]))
    n -= (abList[i+1][0] - abList[i][1])
    if n <= 0:
        print("No")
        exit()
print("Yes")
