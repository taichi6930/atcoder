n = int(input())
a = 1

for b in range(n):
    b = int(input())
    a = a*b//gcd(a, b)

print(a)
