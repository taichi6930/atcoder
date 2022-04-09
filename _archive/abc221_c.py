n = list(input())
lenN = len(n)
ans = 0

for i in range(1, 2 ** lenN - 1):
    a, b = [], []
    for j in range(lenN):
        d = i >> j & 1
        if d:
            a.append(n[j])
        else:
            b.append(n[j])
    ans = max(ans, int(''.join(sorted(a, reverse=True)))
              * int(''.join(sorted(b, reverse=True))))

print(ans)
