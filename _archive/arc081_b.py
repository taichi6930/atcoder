n = int(input())

S1 = list(input())
S2 = list(input())

S = []

cnt = 0
for i in range(n):
    if cnt == n:
        break
    if S1[cnt] == S2[cnt]:
        S.append('a')
        cnt += 1
        continue
    S.append('b')
    cnt += 2

ans = 6 if S[0] == 'b' else 3

for i in range(len(S) - 1):
    if S[i + 1] == 'a' and S[i] == 'a':
        ans *= 2
    if S[i + 1] == 'b' and S[i] == 'b':
        ans *= 3
    if S[i + 1] == 'b' and S[i] == 'a':
        ans *= 2
    ans = ans % (10 ** 9 + 7)

print(ans)
