x, k = map(int, input().split())
x = list(map(int, list('0' + str(x))))
n = len(x)
if k >= n:
    print(0)
    exit()

for i in reversed(range(n - k, n)):
    if x[i] >= 5:
        x[i - 1] += 1
    x[i] = 0

for i in reversed(range(1, n - k)):
    if x[i] >= 10:
        x[i - 1] += 1
    x[i] %= 10

for start in range(n):  # 先頭の0は除外する
    if x[start] != 0:
        break

for i in range(start, n):
    print(x[i], end="")
