from collections import Counter


def str2intWithArray(Array):  # 文字の配列を数字の配列に変換する
    return list(map(lambda x: int(x), Array))


n = int(input())
k = {i: [] for i in range(10)}

for i in range(n):
    S = str2intWithArray(list(input()))
    for j, s in enumerate(S):
        k[s].append(j)

ans = 10 ** 9

for i in range(10):
    ansi = 0
    cK = Counter(k[i])
    for key in list(cK.keys()):
        ansi = max(ansi, key + 10 * (cK[key] - 1))

    ans = min(ans, ansi)
print(ans)
