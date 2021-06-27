# import math


# def comb(n, r):
#     return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


n, l = map(int, input().split())
ans = 0
a = [0] * (n + 1)

# for numL in range(n):
#     num1 = n - numL * l
#     if numL > n or num1 < 0:
#         break
#     com = (comb((num1 + numL), min(numL, num1))) % (10 ** 9 + 7)
#     ans = (ans + com) % (10 ** 9 + 7)

# print(ans)

for i in range(n + 1):
    if i < l:
        a[i] = 1
        continue
    a[i] = (a[i - 1] + a[i - l]) % (10 ** 9 + 7)

print(a[- 1])
