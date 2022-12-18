from pprint import *
n = int(input())
md = [list(map(int, input().split('/'))) for _ in range(n)]
swi = False
months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = [[0 for _ in range(i)] for i in months]
for i, [m, d] in enumerate(md):
    year[m - 1][d - 1] += 1
weekday = 5
for i in range(12):
    for j in range(months[i]):
        weekday = (weekday + 1) % 7
        year[i][j] += 1 if weekday > 4 else 0

ye = []
for m in year:
    ye += m

for i, y in enumerate(ye):
    if i == 365:
        ye[-1] = min(1, y)
        break
    if y > 1:
        ye[i + 1] += y - 1
        ye[i] = 1

for i, y in enumerate(ye):
    if i == 365:
        ye[-1] = min(1, y)
        break
    if y > 1:
        ye[i + 1] += y - 1
        ye[i] = 1
print(ye)
