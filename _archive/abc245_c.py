n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB = [set([A[0], B[0]])] + [set([]) for _ in range(n - 1)]

for i in range(n - 1):
    a = A[i + 1]
    b = B[i + 1]
    ab = AB[i]
    for j in ab:
        if abs(a - j) <= k:
            AB[i + 1].add(a)
        if abs(b - j) <= k:
            AB[i + 1].add(b)
print('Yes' if len(AB[-1]) > 0 else 'No')
