n, m, x = map(int, input().split())
cnt = sum(x > i for i in list(map(int, input().split())))
print(min(cnt, m - cnt))
