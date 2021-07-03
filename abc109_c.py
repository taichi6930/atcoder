import math

n, x = map(int, input().split())
xList = list(map(int, input().split()))
yList = [abs(x - xList[i]) for i in range(n)]

ans = yList[0]
for j in range(n):
    ans = math.gcd(ans, yList[j])
print(ans)
