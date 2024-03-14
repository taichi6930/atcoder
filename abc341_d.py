n, m, k = map(int, input().split())


# 最小公倍数を求める
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


gcdNM = n * m // gcd(n, m)

# n の倍数の個数
cntN = gcdNM // n - 1
# m の倍数の個数
cntM = gcdNM // m - 1
cntNM = cntN + cntM
print(cntNM)

print([(c + 1) * n for c in range(cntN)])
print([(c + 1) * m for c in range(cntM)])


# listNM = sorted(
#     list(set([(c + 1) * n for c in range(cntN)] + [(c + 1) * m for c in range(cntM)]))
# )
# print(((k - 1) // cntNM) * gcdNM + listNM[(k - 1) % cntNM])
