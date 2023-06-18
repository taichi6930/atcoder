n = int(input())
S = [input() for _ in range(n)]
ANS = [1 for _ in range(n)]

for i in range(n):
    s = S[i]
    if s == 'AND':
        ANS[i] = ANS[i - 1]
    else:
        ANS[i] = ANS[i - 1] + 2 ** (i + 1)

print(ANS[-1])
