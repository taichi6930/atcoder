from pprint import pprint
h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]
ansList = [[0 for i in range(w)] for _ in range(h)]

for i in range(h):
    for j in range(w):
        if S[i][j] == '#':
            for a in range(3):
                for b in range(3):
                    if i + a - 1 < 0 or i + a - 1 >= h or j + b - 1 < 0 or j + b - 1 >= w:
                        continue
                    ansList[i + a - 1][j + b - 1] += 1

for i in range(h):
    for j in range(w):
        print('#' if S[i][j] == '#' else ansList[i][j], end="")
    print('')
