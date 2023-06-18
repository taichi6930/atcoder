from collections import *
s = list(input())
cS = Counter(s)

pair = 0
alone = 0

for i, k in enumerate(cS.keys()):
    q = cS[k]
    alone += q % 2
    pair += q // 2

print(pair * 2 if alone == 0 else 1 + 2 * int(pair / alone))
