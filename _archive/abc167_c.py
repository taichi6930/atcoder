def is_nth_bit_set(num: int, k: int):
    if num & (1 << k):
        return True
    return False


n, m, x = map(int, input().split())
cList = []
aList = []

for _ in range(n):
    ca = list(map(int, input().split()))
    cList.append(ca[0])
    aList.append(ca[1:])

ans = -1

for i in range(2 ** n):
    ansz = 0
    z = [0] * m
    for j in range(n):
        if is_nth_bit_set(i, j):
            ansz += cList[j]
            for k in range(m):
                z[k] += aList[j][k]
    if min(z) >= x:
        if ans < 0:
            ans = ansz
            continue
        ans = min(ans, ansz)

print(ans)
