n = int(input())
a = list(map(int, input().split()))
b = sorted(a, reverse=True)
for i in range(n):
    print(a.index(b[i]) + 1)
