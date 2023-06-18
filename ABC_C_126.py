import math

N, K = map(int, input().split())

# print(N)
# print(K)

A = 0
B = []

a = 0

for n in range(1, N+1):
    if K/n > 1:
        i = math.ceil(math.log2(K/n))
        a += 2 ** (N+1-i)
        B.append(a)
    else:
        a += 2 ** (N+1) * (N + 1-n)
        break

# for n in range(1, N+1):
#     if K/n <= 1:
#         i = 0
#     else:
#         i = math.ceil(math.log2(K/n))
#     a += 2 ** (N+1-i)

    #A += 1/(2**i)
# print(A)
# print(A*(1/N))

print(a/(2**(1+N))/N)
