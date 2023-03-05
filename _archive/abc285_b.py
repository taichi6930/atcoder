n = int(input())
S = input()

for i in range(1, n):
    ans = 0
    for j in range(n - i):
        if S[j] == S[i + j]:
            break
        ans += 1
    print(ans)
