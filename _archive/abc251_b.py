n, w = map(int, input().split())
A = list(map(int, input().split()))

ansSet = set()

for a in A:
    if a <= w:
        ansSet.add(a)

for i in range(n - 1):
    for j in range(i + 1, n):
        k = A[i] + A[j]
        if k <= w:
            ansSet.add(k)

for h in range(n - 2):
    for i in range(h + 1, n - 1):
        for j in range(i + 1, n):
            k = A[i] + A[j] + A[h]
            if k <= w:
                ansSet.add(k)


print(len(ansSet))
