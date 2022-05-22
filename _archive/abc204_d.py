n = int(input())
T = sorted(list(map(int, input().split())), reverse=True)
t1 = 0
t2 = 0

for t in T:
    if t1 < t2:
        t1 += t
        continue
    t2 += t

print(max(t1, t2))
