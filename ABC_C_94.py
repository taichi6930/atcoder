n = int(input())
x = list(map(int, input().split()))
xSort = sorted(x)
a, b = xSort[n//2-1], xSort[n//2]
for i in x:
    print(a if i >= b else b)
