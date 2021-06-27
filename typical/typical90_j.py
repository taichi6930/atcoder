n = int(input())
a1 = [0] * (n + 1)
a2 = [0] * (n + 1)
for i in range(1, n + 1):
    c, p = map(int, input().split())
    a1[i] = a1[i - 1]
    a2[i] = a2[i - 1]
    if c == 1:
        a1[i] += p
    else:
        a2[i] += p

q = int(input())
for j in range(q):
    l, r = map(int, input().split())
    print(a1[r] - a1[l - 1], a2[r] - a2[l-1])
