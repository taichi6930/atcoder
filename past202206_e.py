import math
n = int(input())
k = int(math.log(n + 1, 2))
a = n - 1 - (2 ** k - 2)
b = 2 ** k
# print(n, k - 1, a, b)
print(min(a + 1, b - a + 1))
# if k - 1 < n - 2 ** k:
#     print(n - 2 ** k + 1 + 2 ** k - (n - 1))
# else:
#     print(n - 2 ** k + 1 + 1)
