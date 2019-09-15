n, m = map(int, input().split())
ab = []
for i in range(m):
    ab.extend(input().split())
for i in range(n):
    print(ab.count(str(i+1)))
