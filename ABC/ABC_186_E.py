t = int(input())

for i in range(t):
    n, s, k = map(int, input().split())
    cnt = 0
    num = n - s
    ncnt = 0
    lis = [0] * 10 ** 10
    for j in range(10**9):
        a = num // k
        cnt += a
        if num == k * a:
            print(cnt)
            break
        p = num % k
        if lis.count(p) > 0:
            print(-1)
            break
        lis[ncnt] = p
        ncnt += 1
        num = n + num % k
