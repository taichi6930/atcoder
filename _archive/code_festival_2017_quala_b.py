n, m, k = map(int, input().split())

for i in range(n + 1):
    for j in range(m + 1):
        if i * (m - j) + j * (n - i) == k:
            print('Yes')
            exit()

print('No')
