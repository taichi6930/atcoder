from collections import Counter
n, m = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(m)]

k = int(input())
CD = [list(map(int, input().split())) for _ in range(k)]
lists = []

for i in range(2 ** k):
    lis = set()
    for j, cd in enumerate(CD):
        lis.add(cd[i >> j & 1])
    lists.append(list(lis))

ans = 0


for lis in sorted(lists, reverse=True):
    cnt = 0
    for ab in AB:
        if ab[0] in lis and ab[1] in lis:
            cnt += 1

    ans = max(cnt, ans)

print(ans)
