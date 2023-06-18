n = int(input())
A = []
minA = 10**10
minANum = 0
for i in range(n):
    s, t = map(str, input().split())
    t = int(t)
    if t <= minA:
        minA = t
        minANum = i
    A.append([s, t])

for j in range(n):
    print(A[(minANum + j) % n][0])
