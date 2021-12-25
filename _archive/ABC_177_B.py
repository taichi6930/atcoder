s = list(input())
t = list(input())

maxSame = 0

for i in range(len(s) - len(t) + 1):
    p = 0
    for j in range(len(t)):
        if s[i + j] == t[j]:
            p += 1
    maxSame = max(p, maxSame)
print(len(t) - maxSame)
