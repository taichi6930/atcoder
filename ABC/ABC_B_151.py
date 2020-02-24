n, k, m = map(int, input().split())
ans = n * m - sum(list(map(int, input().split())))
if ans <= 0:
    print(0)
elif ans <= k:
    print(ans)
else:
    print(-1)
