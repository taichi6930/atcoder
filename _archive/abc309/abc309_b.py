n = int(input())
A = [list(input()) for _ in range(n)]
for i, a in enumerate(A):
    l = []
    if i == 0:
        l = A[1][:1] + A[0][:-1]
    elif i == n - 1:
        l = A[-1][1:] + A[-2][-1:]
    else:
        l = A[i + 1][:1] + A[i][1:-1] + A[i - 1][-1:]
    print("".join(l))
