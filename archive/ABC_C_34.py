def cmb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


w, h = map(int, input().split())
w -= 1
h -= 1
print(cmb((w+h), h) % 1000000007)
# a = 1
# b = 1
# for i in range(0, h - 1):
#     a *= w + h - 2 - i
#     b *= h - i

# print(int(a/b) % 1000000007)
