n, m = map(int, input().split())
kvList = {i: i for i in range(n + 1)}  # どの場所にどのCDがあるか
vkList = {i: i for i in range(n + 1)}  # どのCDがどの場所にあるか
for i in range(m):
    # CDの数字が入力される
    x = int(input())

    # CDがどの場所にあるかをvkListから探す
    xPlace = vkList[x]

    # 次の場所を計算する
    yPlace = 0

    # 次の場所にある数字をkvListから探す
    y = kvList[yPlace]

    # listにある数字を全てswapする
    kvList[xPlace], kvList[yPlace] = y, x
    vkList[x], vkList[y] = yPlace, xPlace


def int2strWithArray(Array):  # 数字の配列を文字の配列に変換する
    return list(map(lambda x: str(x), Array))


for i in range(n):
    print(kvList[i + 1])
