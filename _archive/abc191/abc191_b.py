n, x = map(int, input().split())
A = list(map(int, input().split()))
aList = [""] * n
q = 0
for i in range(n):
    if A[i] != x:
        aList[q] = str(A[i])
        q += 1

print(" ".join(aList))
