from pprint import pprint
S = [list(input()) for _ in range(9)]
cnt = 0

for i in range(9):
    for j in range(9):
        if S[i][j] == '.':
            continue
        for a in range(i, 9):
            for b in range(j + 1, 9):
                if i == a and b == j:
                    continue
                if S[a][b] == '.':
                    continue
                dx = a - i
                dy = b - j
                if not(0 <= a + dy < 9):
                    continue
                if not(0 <= b - dx < 9):
                    continue
                if S[a + dy][b - dx] == '.':
                    continue
                if not(0 <= i + dy < 9):
                    continue
                if not(0 <= j - dx < 9):
                    continue
                if S[i + dy][j - dx] == '.':
                    continue
                cnt += 1

print(cnt)
