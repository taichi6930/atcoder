from collections import deque
n, m = map(int, input().split())

AB = [list(map(int, input().split())) for _ in range(m)]
ab2List = {}
ab1List = {}

for _, [a, b] in enumerate(AB):
    # ab2Listに入っている場合、OUT
    if a in ab2List or b in ab2List:
        print('No')
        exit()

    # ab1Listに入っている場合、削除してab2Listに移行する
    if a in ab1List:
        ab1List[a].append(b)
        ab2List[a] = ab1List.pop(a)
    else:
        ab1List[a] = [b]

    if b in ab1List:
        ab1List[b].append(a)
        ab2List[b] = ab1List.pop(b)
    else:
        ab1List[b] = [a]


for key in list(ab2List.keys()):
    k = deque([ab2List[key][0], key, ab2List[key][1]])
    print(k, ab2List, ab1List)

    for kee in ab2List[key]:
        if kee in ab2List:
            ab2List[kee].remove(key)
            ab1List[kee] = ab2List[kee]
            ab2List.pop(kee)
            continue
        if kee in ab1List:
            ab1List.pop(kee)
            continue
    ab2List.pop(key)

    for i in range(2):
        for j in range(10 ** 9):
            kk = k[-1]
            if kk in ab2List:
                print(k, ab2List, ab1List)
                print('No')
                exit()
            if not kk in ab1List:
                break
            k.append(ab1List[kk][0])
            ab1List.pop(kk)

        k = deque(list(k)[::-1])
