n = int(input())
A = list(map(int, input().split()))

B = [0] * (n - int(n / 2)) + A[int((n - 1) / 2) + 1:]

for i in range(n - int(n / 2), 0, -1):
    k = 0
    for j in range(1, 10 ** 6):
        w = i * (j + 1) - 1
        if w >= n:
            break
    if k % 2 != A[i - 1]:
        B[i - 1] = 1

print(sum(B))
strAns = ''
swi = False

for i, b in enumerate(B):
    if b == 1:
        swi = True
        strAns += str(i + 1) + ' '

if swi:
    print(strAns)
