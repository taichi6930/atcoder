from itertools import accumulate
n = int(input())
A = sorted(list(map(int, input().split())))
B = list(accumulate(A))
sumA = sum(A)

ans = sumA / n
k = 0

for i, a in enumerate(A):
    x = a * 0.5
    ans = min(ans, (n * x + sumA - B[i] - 2 * x * (n - i - 1)) / n)

print(ans)
