import abc


n = int(input())
abcList = list(map(int, input().split()))
a, b, c = max(abcList), sum(abcList) - \
    max(abcList) - min(abcList), min(abcList)
ans = 10 ** 5

for i in range(10 ** 4):
    for j in range(10 ** 4):
        if i + j > 9999:
            break
        k = n - i * a - j * b
        if k < 0:
            break
        if k % c == 0:
            ans = min(ans, i + j + k // c)
print(ans)
