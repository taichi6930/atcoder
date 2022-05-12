from collections import Counter
from math import gcd
n = int(input())
A = sorted(list(map(int, input().split())))

k = A[0]
for i in range(n - 1):
    k = gcd(A[i + 1], k)

if k > 1:
    print('not coprime')
    exit()


def prime_factorization(n):  # 素因数分解を行う
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


setA = set()
setALen = 0

for a in A:
    if a == 1:
        continue
    newSetA = set(Counter(prime_factorization(a)).keys())
    newSetALen = len(newSetA)
    addSetA = setA | newSetA
    if len(addSetA) != setALen + newSetALen:
        print('setwise coprime')
        exit()
    setA = addSetA
    setALen = len(addSetA)

print('pairwise coprime')
