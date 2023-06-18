n, m = map(int, input().split())
B = [n - i for i in range(n)]
for _ in range(m):
    a = int(input())
    B.append(a)
bSet = set()

for i, b in enumerate(B[::-1]):
    if b in bSet:
        continue
    bSet.add(b)
    print(b)
