from collections import Counter
n = int(input())
S = [input() for _ in range(n)]
cS = Counter()

for i, s in enumerate(S):
    print(s + '(' + str(cS[s]) + ')' if s in cS else s)
    cS[s] += 1
