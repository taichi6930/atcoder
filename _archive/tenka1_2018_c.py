n = int(input())
A = sorted([int(input()) for _ in range(n)], reverse=True)

print(
    sum(A[: n // 2 - 1]) * 2 + sum([A[n // 2 - 1]]) -
    sum([A[n // 2]]) - sum(A[n // 2 + 1:]) * 2
    if n % 2 == 0
    else max(sum(A[: n // 2 - 1]) * 2 + sum([A[n // 2 - 1]]) + sum([A[n // 2]]) - sum(A[n // 2 + 1:]) * 2, sum(A[: n // 2]) * 2 - sum([A[n // 2]]) - sum([A[n // 2 + 1]]) - sum(A[n // 2 + 2:]) * 2)
)
