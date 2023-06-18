from collections import Counter
import math


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


n = int(input())
A = list(map(int, input().split()))

a_gcd = A[0]
for i in range(1, n):
    a_gcd = math.gcd(a_gcd, A[i])

cnt = 0
for a in A:
    cA = Counter(prime_factorization(a // a_gcd))
    if cA[2] > 0:
        cnt += cA[2]
        cA.pop(2)
    if cA[3] > 0:
        cnt += cA[3]
        cA.pop(3)
    if len(cA) > 0:
        exit(print(-1))

print(cnt)
