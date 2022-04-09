from collections import Counter, deque
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cB = Counter(B)

ans1, ans2 = 0, 0

for i in range(n):
    if A[i] == B[i]:
        ans1 += 1
        continue
    if cB[A[i]] > 0:
        ans2 += 1

print(ans1)
print(ans2)
