from collections import defaultdict, Counter


def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


n, m = map(int, input().split())

dic = defaultdict(str)

for i in range(m):
    c = int(input())
    A = list(map(str, input().split()))
    old_dic = dic.copy()
    for key, value in old_dic.items():
        value_split = value.split('_')
        new_value = set(value_split) | set(A)
        new_value_str = '_'.join(int2strWithArray(
            sorted(str2intWithArray(list(new_value)))))
        new_key_str = f'{key}_{i}'
        dic[new_key_str] = new_value_str
    dic[str(i)] = '_'.join(A)

ans_str = '_'.join([str(i + 1) for i in range(n)])

print(Counter(dic.values())[ans_str])
