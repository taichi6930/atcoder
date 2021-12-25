n, k = map(int, input().split())
abList = [None] * 2 * n

for i in range(n):
    a, b = map(int, input().split())
    abList[2 * i], abList[2 * i + 1] = a - b, b

abList.sort(reverse=True)
print(sum(abList[:k]))
