S = list(input())
swi = "="
num = 0
ans = 0
A = []

for i in range(len(S)):
    s = S[i]
    if s != swi:
        A.append([num, swi])
        num = 0
        swi = s
    num += 1
    if i == len(S) - 1:
        A.append([num, swi])
        break

print(A)

for j in range(len(A) - 1):
    if A[j][0] == 0:
        continue
    if A[j][1] == ">":
        ans += ((A[j][0] + 1) * A[j][0]) // 2
    if A[j][1] == "<":
        ans += ((A[j][0] - 1) * A[j][0]) // 2
    print(ans, A[j])

ans += ((A[-1][0] + 1) * A[-1][0]) // 2

print(ans)
