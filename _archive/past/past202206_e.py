n = int(input())
j = int((-1 + (1 + 4 * (n - 1)) ** 0.5) / 2)
print(min((j + 1) * (j + 2) + 2 - n, n - (j) * (j + 1)))
