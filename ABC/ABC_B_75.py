H, W = map(int, input().split())
ans = []
for h in range(H+2):
    ans.append([0] * (W + 2))
qu = []
for h in range(H):
    qu.append(input())

for h in range(H):
    for w in range(W):
        if qu[h][w] == "#":
            for i in range(3):
                for j in range(3):
                    if ans[h+i][w+j] != "#":
                        ans[h+i][w+j] += 1
            ans[h+1][w+1] = "#"

for h in range(H):
    result = map(str, ans[h+1][1:W+1])
    print(''.join(result))
