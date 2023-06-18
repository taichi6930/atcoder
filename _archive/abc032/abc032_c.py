n, k = map(int, input().split())
S = [int(input()) for _ in range(n)]

if S.count(0) > 0:
    print(n)
    exit()
ans = 0
p = S[0]
st, gl = 0, 0

for _ in range(n ** 2):
    if gl >= n:
        break
    if p > k:
        p = p // S[st]
        st += 1
        if st + ans >= n:
            break
    else:
        ans = max(ans, gl - st + 1)
    gl += 1
    if gl >= n:
        break
    p *= S[gl]

print(ans)
