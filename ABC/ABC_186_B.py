h, w = map(int, input().split())
sumA = 0
minA = 100

for i in range(h):
    A = list(map(int, input().split()))
    minA = min(minA, min(A))
    sumA += sum(A)

print(sumA - minA * h * w)
