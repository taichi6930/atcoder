import math


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


n = int(input())
ans = 0
if n != 1:
    for f in factorization(n):
        ans += int((-1 + (1 + 8 * f[1]) ** 0.5) / 2)

print(ans)
