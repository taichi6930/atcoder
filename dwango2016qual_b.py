n = int(input())
K = list(map(int, input().split()))
J = [0] * n

for i in range(n):
    if i == 0:
        J[i] = K[i]
        J[i + 1] = K[i]
        continue
    if i == n - 1:
        J[i] = K[i - 1]
        continue
    if J[i + 1] != K[i - 1]:
        J[i + 1] = K[i]
print(J)
