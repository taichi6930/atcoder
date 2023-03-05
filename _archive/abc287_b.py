n, m = map(int, input().split())
S = [input()[-3:] for _ in range(n)]
T = [input() for _ in range(m)]
cnt = 0

for s in S:
    swi = False
    for t in T:
        if s != t:
            continue
        swi = True
        break
    if swi:
        cnt += 1

print(cnt)
