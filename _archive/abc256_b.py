n = int(input())
A = list(map(int, input().split()))
p = 0
M = [0, 0, 0, 0]
for i, a in enumerate(A):
    M[0] += 1
    for j in range(3, -1, -1):
        if j + a >= 4:
            p += M[j]
        else:
            M[j + a] = M[j]
        M[j] = 0

print(p)
