from math import gcd
n = int(input())
A = list(map(int, input().split()))

gc = 1
for i, a in enumerate(A):
    gc = a * gc // gcd(a, gc)

print(sum([(gc - 1) % a for a in A]))
