n, x = map(int, input().split())
alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

st = ''
for al in alpha:
    st += al * n

print(st[x - 1])
