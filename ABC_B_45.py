s = list([input() for _ in range(3)])
alphaList = ["a", "b", "c"]
ALPHAList = ["A", "B", "C"]
swi = "a"
while len(s[0]) * len(s[1]) * len(s[2]) >= 0:
    # 選んだカードが一枚もなかったら終了
    if len(s[alphaList.index(swi)]) == 0:
        print(ALPHAList[alphaList.index(swi)])
        break

    # 次のカード
    nextSwi = s[alphaList.index(swi)][0]

    # 不要なカードを消す
    sLen = len(s[alphaList.index(swi)])
    s[alphaList.index(swi)] = s[alphaList.index(swi)][1:sLen]

    swi = nextSwi
