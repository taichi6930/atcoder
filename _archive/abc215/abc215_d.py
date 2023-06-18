from collections import *


def prime_factorization(n):
    """
    task:prime factorization
    return:prime
    type:list
    """
    lis = []
    for i in range(2, int(n ** 0.5) + 1):
        while True:
            if n % i == 0:
                lis.append(i)
                n = n // i

            else:
                break

    if n > int(n ** 0.5):
        lis.append(n)

    return lis


n, m = map(int, input().split())
A = list(map(int, input().split()))
primeSet = set()
for a in A:
    primeSet |= set(list(Counter(prime_factorization(a)).keys()))

primeTF = [False] + [True] * (m)
ans = 0

for i in list(primeSet):
    for j in range(10 ** 9):
        if i * (j + 1) >= m + 1:
            break
        primeTF[i * (j + 1)] = False

ansList = []

for i, pf in enumerate(primeTF):
    if pf:
        ansList.append(i)

print(len(ansList))
for ans in ansList:
    print(ans)
