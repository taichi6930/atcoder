n, q = map(int, input().split())
kvList = {i: i for i in range(1, n + 1)}  # どの場所にどのボールがあるか
vkList = {i: i for i in range(1, n + 1)}  # どのボールがどの場所にあるか
for i in range(q):
    # ボールの数字が入力される
    x = int(input())

    # ボールがどの場所にあるかをvkListから探す
    xPlace = vkList[x]

    # 次の場所を計算する
    yPlace = xPlace + 1 if xPlace != n else xPlace - 1

    # 次の場所にある数字をkvListから探す
    y = kvList[yPlace]

    # listにある数字を全てswapする
    kvList[xPlace], kvList[yPlace] = y, x
    vkList[x], vkList[y] = yPlace, xPlace


def int2strWithArray(Array):  # 数字の配列を文字の配列に変換する
    return list(map(lambda x: str(x), Array))


print(' '.join(int2strWithArray([kvList[i + 1] for i in range(n)])))
