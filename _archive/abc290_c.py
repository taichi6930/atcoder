n, k = map(int, input().split())
A = tuple(map(int, input().split()))
setA = set(A)

for i in range(k):
    if i in setA:
        continue
    exit(print(i))
print(k)
