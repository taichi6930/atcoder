from collections import deque
n = int(input())
A = deque(sorted(list(map(int, input().split()))))
k = n
ans = 0

for i in range(n):
    if k == 0:
        break
    if A[0] == i + 1:
        k -= 1
        ans += 1
        A.popleft()
        continue
    for j in range(2):
        if k == 0:
            break
        k -= 1
        A.pop()
        if j == 1:
            ans += 1

print(ans)
