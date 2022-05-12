
from copy import deepcopy


def is_nth_bit_set(num: int, k: int):
    if num & (1 << k):
        return True
    return False


ans = 0
h, w, kk = map(int, input().split())
c = []

# 全てをつなげる
for _ in range(h):
    a = []
    Z = list(input())
    for z in Z:
        a.append(1 if z == '#' else 0)
    c.append(a)

print('c: ', c)

for i in range(2 ** h):
    cc = deepcopy(c)
    for j in range(h):
        if is_nth_bit_set(i, j):
            for k in range(w):
                cc[j][k] = 0

    for l in range(2 ** w):
        for p in range(w):
            ccc = deepcopy(cc)
            if is_nth_bit_set(l, p):
                for q in range(h):
                    cc[q][p] = 0
            sumc = sum([sum(ccc[w]) for w in range(h)])
        if sumc == kk:
            print(j)
            ans += 1


print(ans)
