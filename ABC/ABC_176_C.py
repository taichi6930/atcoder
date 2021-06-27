n = int(input())
A, aMax, aSum = list(map(int, input().split())), 0, 0

for i in range(n):
    if aMax <= A[i]:
        aMax = A[i]
        continue
    aSum += aMax - A[i]
print(aSum)
