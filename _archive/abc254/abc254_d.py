from collections import Counter
n = int(input())

# 素数を使った解き方は
primeTF = [False, False] + [True] * (n - 1)
ans = 0

primeList = []
for i in range(n + 1):
    if primeTF[i]:
        primeList.append(i)
        for j in range(n + 1):
            if i * (j + 2) >= n + 1:
                break
            primeTF[i * (j + 2)] = False

primeSet = set(primeList)


def prime_factorization(n):
    if n == 1:
        return []
    if n in primeSet or n == 1:
        return [n]
    for prime in primeList:
        if prime ** 2 > n:
            break
        if n % prime == 0:
            return [prime] + prime_factorization(n // prime)


for i in range(n):
    kList = []
    kk = 1
    cP = Counter(prime_factorization(i + 1))
    for key in list(cP):
        if cP[key] % 2 == 1:
            kList.append(key)
            kk *= key
    ans += int((n / kk) ** 0.5)
print(ans)
