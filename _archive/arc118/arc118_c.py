from collections import deque
n = int(input())
s = [6, 10, 15]


def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


t = set()

for i in range(10000):
    t.add(s[i % 3] * (1 + (i + 3) // 3))

print(' '.join(int2strWithArray(s + sorted(list(t)))[:n]))
