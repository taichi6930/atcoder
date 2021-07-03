import math

n = int(input())
m = int(math.sqrt(n))
for i in range(m):
    k = m-i
    if n % k == 0:
        print(max(len(str(k)), len(str(n // k))))
        break
