import fractions

a, b, c = map(int, input().split())
k = fractions.gcd(a, b, c)
print((a + b + c) // k - 3)
