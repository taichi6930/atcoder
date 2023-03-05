
from collections import Counter
n = int(input())
mod = 10 ** 9 + 7
if n == 1:
    exit(print(1))


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


c = Counter()

for i in range(2, n + 1):
    lis = prime_factorization(i)
    for j in lis:
        c[j] += 1

ans = 1

for key in list(c.keys()):
    ans = (ans * (c[key] + 1)) % mod

print(ans)
