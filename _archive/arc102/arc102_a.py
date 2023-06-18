n, k = map(int, input().split())
ans = (n // k) ** 3
cnt = 0


print(ans + sum([1 if i % k == k // 2 and k %
      2 == 0 else 0 for i in range(1, n + 1)]) ** 3)
