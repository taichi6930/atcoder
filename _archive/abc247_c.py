def int2strWithArray(Array):  # 数字の配列を文字の配列に変換する
    return list(map(lambda x: str(x), Array))


n = int(input())
s = [[1]]
for i in range(n - 1):
    s.append(s[-1] + [i + 2] + s[-1])

print(' '.join(int2strWithArray(s[-1])))
