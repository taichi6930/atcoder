n = int(input())
print(sum(max(n - 10 ** ((i + 1) * 3) + 1, 0)for i in range(5)))
