n, x = map(int, input().split())
m = [int(input()) for _ in range(n)].sort()
print(n + int((x - sum(m))/m[0]))
