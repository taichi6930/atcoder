n, k = map(int, input().split())
abcSum = 0
for a in range(1, n+1):
    for b in range(a, n+1):
        if (a + b) % k == 0 and (2 * b) % k == 0:
            if a == b:
                abcSum += 1
            else:
                abcSum += 6
        if abcSum % 6 == 0:
            print(abcSum)

print(abcSum)
