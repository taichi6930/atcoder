n, a, b, c, d = map(int, input().split())
S = list(input())
stoneList = []

for i, s in enumerate(S):
    if s == '#':
        stoneList.append(i + 1)
        if len(stoneList) <= 1:
            continue
        if stoneList[-1] - stoneList[-2] == 1:
            print('No')
            exit()


# c,d どちらか大きい値に辿り着くまでに、石が二つ並んでいたらその時点でNo
print(stoneList)
