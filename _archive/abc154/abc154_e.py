n = int(input())
k = int(input())
ans = 0
strN = str(n)


def cmb(n, r, m=None):
    from functools import reduce
    from operator import mul

    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    if m is None:
        return over // under
    return (over // under) % m


# 桁が1つ少ないものまでを先に計算する
print(len(strN) - 1, k)
ans += cmb(len(strN) - 1, k) * 9**k

# for i in range(len(strN)):
#     if strN[i] == 0:
#         continue
#     if strN[]
#     print(i)
print(ans)
