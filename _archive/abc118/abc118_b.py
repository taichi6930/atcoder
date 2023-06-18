n, m = map(int, input().split())
b = []
a = [b.extend(list(map(int, input().split()))[1::]) for _ in range(n)]
num = 0
for i in range(m):
    if b.count(i + 1) == n:
        num += 1

print(num)
