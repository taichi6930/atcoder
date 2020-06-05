n = int(input())
p = list(map(int, input().split()))
sumN = 0
maxN = max(p)

for i in range(n):
    if p[i] <= maxN:
        sumN += 1
        maxN = p[i]
        if maxN == 1:
            break

print(sumN)
