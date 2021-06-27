n = int(input())
ans = "No"
xy = [None] * n
for i in range(n):
    xy[i] = list(map(int, input().split()))

for a in range(n - 2):
    for b in range(a+1, n - 1):
        for c in range(b + 1, n):
            if (xy[c][1] - xy[a][1]) * (xy[b][0] - xy[a][0]) == (xy[b][1] - xy[a][1]) * (xy[c][0] - xy[a][0]):
                ans = "Yes"


print(ans)
