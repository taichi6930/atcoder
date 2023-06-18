from collections import defaultdict
n, k, d = map(int, input().split())
A = sorted(list(map(int, input().split())))
dic = defaultdict()
dic[f'{k}_0'] = 0

for i, a in enumerate(A):
    old_dic = dic.copy()
    dic = defaultdict()
    for key, value in old_dic.items():
        # 足さない
        dic[key] = max(dic[key], value) if key in dic else value
        # 足す
        n_num, n_mod = map(int, key.split('_'))
        if n_num <= 0:
            continue
        new_key = f'{n_num - 1}_{(n_mod + a) % d}'
        new_value = value + a
        dic[new_key] = max(
            dic[new_key], new_value) if new_key in dic else new_value

print(dic['0_0'] if '0_0' in dic else -1)
