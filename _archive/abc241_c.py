n = int(input())
S = [list(input()) for _ in range(n)]
aList = [[1, -1], [1, 0], [1, 1], [0, 1]]
ans = False


def test(i, j, a):
    cnt = 0
    for k in range(6):
        ii = i + a[0] * k
        jj = j + a[1] * k
        if not(0 <= ii < n) or not(0 <= jj < n):
            return
        q = S[ii][jj]
        if q == '#':
            cnt += 1

    if cnt >= 4:
        print('Yes')
        exit()


for i in range(n - 2):
    for j in range(n - 2):
        for a in aList:
            test(i, j, a)

print('No')
