n, k = map(int, input().split())
s = input()

if k > 5000 * 26:
    k = 5000 * 26

if k != 1:
    for i in range(k - 1):
        sList = []
        t = (s[::-1])
        u = s + t
        for j in range(0, n+1):
            sList.append((u[j:(j + n)])[::-1])
        sList.sort()
        if s == sList[0][::-1]:
            break
        s = sList[0][::-1]


for i in range(1):
    sList = []
    t = (s[::-1])
    u = s + t
    for j in range(0, n+1):
        sList.append(u[j:(j + n)])
    sList.sort()
    s = sList[0]

print(s)
