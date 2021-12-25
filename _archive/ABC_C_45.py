s = list(input())
n = len(s) - 1
sumS = 0

patterns = []
for i in range(2 ** n):
    tmp = [False] * n
    for j in range(n):
        if i >> j & 1:
            tmp[j] = True
    patterns.append(tmp)

for pattern in patterns:
    a = s[0]
    for i in range(len(pattern)):
        if pattern[i] == True:
            sumS += int(a)
            a = "0"
        a += s[i+1]
    sumS += int(a)

print(sumS)
