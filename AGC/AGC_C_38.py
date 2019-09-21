import fractions

n = int(input())
a = list(map(int, input().split()))
aSum = 0
for i in range(0, n-1):
    aSum += sum((a[i] * a[j] // fractions.gcd(a[i], a[j])) %
                998244353 for j in range(i + 1, n))
print(aSum)
