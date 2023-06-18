import collections
n = int(input())
[a, b, c] = [list(map(int, input().split())) for _ in range(3)]

ans = 0

for i in range(n):
    a[i], b[i], c[i] = a[i] % 46, b[i] % 46, c[i] % 46


aC = collections.Counter(a)
bC = collections.Counter(b)
cC = collections.Counter(c)

for x in aC.keys():
    for y in bC.keys():
        for z in cC.keys():
            if(x + y + z) % 46 == 0:
                ans += aC[x] * bC[y] * cC[z]
print(ans)
