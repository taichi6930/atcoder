from collections import Counter
A, B, C = map(int, input().split())


def int2strWithArray(Array):  # 数字の配列を文字の配列に変換する
    return list(map(lambda x: str(x), Array))


lis = Counter()

# Aが最後に決まる時
for b in range(100 - B):
    for c in range(100 - C):
        a = 100 - A
        lis['-'.join(int2strWithArray(sorted([a, b, c])))] += 1
print(lis)

# Bが最後に決まる時
for c in range(100 - C):
    for a in range(100 - A):
        b = 100 - B
        lis['-'.join(int2strWithArray(sorted([a, b, c])))] += 1
print(lis)

# Cが最後に決まる時
for a in range(100 - A):
    for b in range(100 - B):
        c = 100 - C
        lis['-'.join(int2strWithArray(sorted([a, b, c])))] += 1
print(lis)

print(A, b, c, lis)
