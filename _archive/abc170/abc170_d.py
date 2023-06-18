
from collections import Counter


def make_divisors(n):
    """
    約数列挙を行う。

    Parameters
    ----------
    n : int
        約数を求めたい数

    Returns
    -------
    divisors : [int]
        約数が昇順に入った配列
    """
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    divisors = lower_divisors + upper_divisors[::-1]
    return divisors


n = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
maxA = max(A)
cA = Counter(A)
cAKeys = sorted(list(cA.keys()))
print(sorted(cAKeys))

cnt = 0
for i in range(len(cAKeys)):
    key = cAKeys[i]
    if cA[key] > 1:
        continue
    if maxA < 2 * key:
        cnt += 1
        continue

    swi = True
    for j in range(len(cAKeys)):
        if i == j:
            continue
        print(cAKeys[i], cAKeys[j], cAKeys[i] % cAKeys[j])
        if cAKeys[i] % cAKeys[j] == 0:
            swi = False
            break
    # print(swi, cAKeys[i])
    if swi:
        cnt += 1
        continue

print(cnt)
