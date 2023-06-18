n, x, y, z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
IAB = [[i + 1, A[i], B[i], A[i] + B[i]] for i in range(n)]

ans = set()

IAB1 = sorted(IAB, key=lambda x: x[1], reverse=True)
for i in range(x):
    ans.add(IAB1[i][0])

IAB2 = sorted(IAB, key=lambda x: x[2], reverse=True)
ycnt = 0
for i in range(n):
    if ycnt == y:
        break
    if IAB2[i][0] in ans:
        continue
    ans.add(IAB2[i][0])
    ycnt += 1

IAB3 = sorted(IAB, key=lambda x: x[3], reverse=True)
zcnt = 0
for i in range(n):
    if zcnt == z:
        break
    if IAB3[i][0] in ans:
        continue
    ans.add(IAB3[i][0])
    zcnt += 1

for an in sorted(list(ans)):
    print(an)
