s = int(input())
sList = [s]
i = 0
while i >= 0:
    if sList[i] % 2 == 0:
        s = sList[i] // 2
    else:
        s = sList[i] * 3 + 1
    sList.append(s)
    if sList[0:i + 1].count(s) == 1:
        print(i + 2)
        break
    i += 1
