n = int(input())
A = sorted(list(set(list(map(int, input().split())) + [0])))

ans = 1

for i in range(len(A) - 1):
    ans = pow(ans * (1 + A[i + 1] - A[i]), 1, 10 ** 9 + 7)


print(ans)
