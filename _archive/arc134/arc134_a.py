n, l, w = map(int, input().split())
A = list(map(int, input().split()))
A.insert(0, - w)
A.append(l)
ans = 0
for i in range(n+1):
    width = A[i+1] - (A[i] + w)
    if width > 0:
        ans += -(- width // w)
print(ans)
