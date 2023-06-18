h, w = map(int, input().split())
r, c = map(int, input().split())
ans = 4
if r in [1, h]:
    ans -= 1
if c in [1, w]:
    ans -= 1
if h == 1:
    ans -= 1
if w == 1:
    ans -= 1
print(ans)
