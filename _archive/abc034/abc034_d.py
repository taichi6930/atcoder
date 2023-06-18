from collections import defaultdict
n, k = map(int, input().split())
wp = [tuple(map(int, input().split())) for _ in range(n)]
dic = defaultdict()

for i, (w, p) in enumerate(wp):
    old_dic = dic.copy()
    solt = w * p / 100
    water = w - solt
    dic[(k - 1, p)] = (solt, water)
    for key, value in old_dic.items():
        if key[0] - 1 < 0:
            continue
        new_solt = solt + value[0]
        new_water = water + value[1]
        new_p = (new_solt) / (new_water + new_solt) * 100

        dic[(key[0] - 1, new_p)] = (new_solt, new_water)

print(dic)
