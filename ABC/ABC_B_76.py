n, k = [int(input()) for _ in range(2)]
a = 1
for i in range(n):
    if a < k:
        a *= 2
    else:
        a += k

print(a)
