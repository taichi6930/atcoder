n = int(input())
a = list(map(int, input().split()))
b = [None] * n
b[0] = str(a.index(1) + 1)
for i in range(1, n):
    b[i] = str(a.index(i + 1) + 1)
print(" ".join(b))
