h, w = map(int, input().split())
G = [list(input()) for _ in range(h)]

lis = set(['1-1'])
i = 1
j = 1

for _ in range(h * w):
    st = G[j - 1][i - 1]
    if st == 'R':
        if i >= w:
            exit(print(j, i))
        i += 1

    if st == 'L':
        if i <= 1:
            exit(print(j, i))
        i -= 1

    if st == 'U':
        if j <= 1:
            exit(print(j, i))
        j -= 1

    if st == 'D':
        if j >= h:
            exit(print(j, i))
        j += 1
    newst = str(i) + '-' + str(j)
    lis.add(newst)

print(-1)
