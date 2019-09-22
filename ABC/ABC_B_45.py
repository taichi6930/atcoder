s = list([input() for _ in range(3)])
alphaList = ["a", "b", "c"]
ALPHAList = ["A", "B", "C"]
swi = "a"
print(s)
while len(s[0]) * len(s[1]) * len(s[2]) > 0:
    if len(s[alphaList.index(swi)]) == 1:
        print(ALPHAList[alphaList.index(swi)])
        break
    else:
        ss = alphaList.index(swi)
        sLen = len(s[alphaList.index(swi)])
        swi, s[alphaList.index(swi)] = s[alphaList.index(
            swi)][0], s[alphaList.index(swi)][1:sLen]
