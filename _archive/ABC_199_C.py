n = int(input())
s = list(input())
q = int(input())

tq = 0

for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        c, d = s[(a - 1 + tq * n) % (2 * n)], s[(b - 1 + tq * n) % (2 * n)]
        s[(a - 1 + tq * n) % (2 * n)], s[(b - 1 + tq * n) % (2 * n)] = d, c
        continue
    if t == 2:
        tq = (tq + 1) % 2
print("".join(s) if tq == 0 else "".join(s[n: 2 * n] + s[0: n]))
