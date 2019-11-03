import math

ans = "No"

n = int(input())
for i in range(1, int(math.sqrt(n) + 1)):
    if n % i == 0 and n // i <= 9:
        ans = "Yes"
        break

print(ans)
