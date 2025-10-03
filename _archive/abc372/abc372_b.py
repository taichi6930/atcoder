import math

m = int(input())

sumA = 0
A = []
i = 0

while i < 20:
    k = int(math.log(m - sumA, 3))
    A.append(k)
    sumA += 3**k
    if m == sumA:
        break
    i += 1

print(len(A))
print(" ".join(map(str, A)))
