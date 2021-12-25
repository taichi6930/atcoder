import collections
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ACounter = collections.Counter(A)
ans = 0

for i in range(n):
    ans += ACounter[B[C[i] - 1]]

print(ans)
