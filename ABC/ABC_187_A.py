A, B = map(str, input().split())
A, B = list(A), list(B)
numA, numB = 0, 0
for a in A:
    numA += int(a)

for b in B:
    numB += int(b)

print(max(numA, numB))
