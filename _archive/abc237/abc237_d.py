from collections import deque
n = int(input())
S = list(input())[::-1]


def int2strWithArray(Array):  # 数字の配列を文字の配列に変換する
    return list(map(lambda x: str(x), Array))


ans = deque([n])

for i, s in enumerate(S):
    if s == 'L':
        ans.append(n - i - 1)
    if s == 'R':
        ans.appendleft(n - i - 1)

print(' '.join(int2strWithArray(list(ans))))
