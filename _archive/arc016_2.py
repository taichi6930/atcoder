n = int(input())
C = [list('.........')] + [list(input()) for _ in range(n)]

ans = 0
for j in range(n):
    ans += sum([1 if (C[j][i] != 'o' and C[j + 1][i] == 'o')
               or (C[j + 1][i] == 'x') else 0 for i in range(9)])

print(ans)