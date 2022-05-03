import math
n = int(input())
A = list(map(int, input().split()))
ans = A[0]

for i in range(n - 1):
    ans = math.gcd(ans, A[i + 1])

print(ans)
