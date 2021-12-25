import math
ans = 10 ** 15

n = int(input())
for i in range(1, int(math.sqrt(n) + 1)):
    if n % i == 0 and ans > n / i:
        ans = int(i + n / i - 2)

print(ans)
