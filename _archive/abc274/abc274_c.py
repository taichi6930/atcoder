n = int(input())
A = list(map(int, input().split()))
ans = [0] * (2 * n + 1)
for i, a in enumerate(A):
    ans[2 * i + 1] = ans[a - 1] + 1
    ans[2 * i + 2] = ans[a - 1] + 1

for k in ans:
    print(k)
