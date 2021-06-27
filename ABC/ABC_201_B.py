n = int(input())
s, t = [None] * n, [None] * n
for i in range(n):
    st = list(map(str, input().split()))
    s[i], t[i] = st[0], int(st[1])
print(s[t.index(sorted(t, reverse=True)[1])])
