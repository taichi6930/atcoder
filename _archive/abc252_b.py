n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

maxA = max(A)
ans = 'No'

for i in range(n):
    if A[i] != maxA:
        continue
    if i + 1 in B:
        ans = 'Yes'
        break

print(ans)
