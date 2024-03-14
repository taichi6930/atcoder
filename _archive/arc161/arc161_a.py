n = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
B = [
    A[(n - 1) // 2 :][i // 2] if i % 2 == 0 else A[: (n - 1) // 2][(i - 1) // 2]
    for i in range(n)
]

for i in range((n - 1) // 2):
    if B[2 * i] >= B[2 * i + 1] or B[2 * i + 1] <= B[2 * i + 2]:
        exit(print("No"))

print("Yes")
