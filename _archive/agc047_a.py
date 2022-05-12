from math import gcd
n = int(input())
A = []

for _ in range(n):
    a = input()
    if a.find('.') == -1:
        A.append([int(a), 1])
        continue
    k = len(a) - a.find('.') - 1
    at = int(a.replace('.', ''))
    ab = 10 ** k
    agcd = gcd(at, ab)
    A.append([at // agcd, ab // agcd])
print(A)
