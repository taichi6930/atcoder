n = int(input())
L, R, X = [] * n, [] * n, [] * n
for _ in range(n):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
    X.append(r)

k = sum(X)
for i, l in enumerate(L):
    r = R[i]
    if r - l >= k:
        X[i] = r - k
        k = 0
        break
    k -= r - l
    X[i] = l

if k == 0:
    print("Yes")
    print(*X)
else:
    print("No")
