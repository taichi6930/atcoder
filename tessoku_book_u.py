from collections import defaultdict

n = int(input())
PAList = [list(map(int, input().split())) for _ in range(n)]

ansDict = defaultdict()
ansDict[0] = defaultdict()
ansDict[0][f"1-{n}"] = 0

for i in range(n - 1):
    ansDict[i + 1] = defaultdict(int)
    for key, value in ansDict[i].items():
        # keyを-で分割、_lと_rに分ける、数値にする
        key_l, key_r = map(int, key.split("-"))
        # lから取る場合
        lPoint = (
            PAList[key_l - 1][1]
            if ((key_l < PAList[key_l - 1][0]) and (PAList[key_l - 1][0] <= key_r))
            else 0
        )
        ansDict[i + 1][f"{key_l + 1}-{key_r}"] = max(
            value + lPoint, ansDict[i + 1][f"{key_l + 1}-{key_r}"]
        )

        # rから取る場合
        rPoint = (
            PAList[key_r - 1][1]
            if ((key_l <= PAList[key_r - 1][0]) and (PAList[key_r - 1][0] < key_r))
            else 0
        )
        ansDict[i + 1][f"{key_l}-{key_r - 1}"] = max(
            value + rPoint, ansDict[i + 1][f"{key_l}-{key_r - 1}"]
        )

print(max(ansDict[n - 1].values()))
