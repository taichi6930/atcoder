n, k = map(int, input().split())
p = list(map(int, input().split()))
pSum = 0
swi = 0
for i in range(n-k+1):
    if p[i:i+k] != sorted(p[i:i+k]):
        pSum += 1
    else:
        swi = 1
print(pSum + swi)
