n = int(input())
c = [int(input()) for _ in range(n)]

sum = 0
for i in range(n - 1):
    if c.index(i + 1) > c.index(i + 2):
        sum += 1
print(sum)
