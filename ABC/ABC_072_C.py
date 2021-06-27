import collections

n = int(input())
a = sorted(list(map(int, input().split())))

c = collections.Counter(a)

ans = 0
for i in c.keys():
    ans = max(ans, c[i] + c[i - 1] + c[i + 1])

print(ans)
