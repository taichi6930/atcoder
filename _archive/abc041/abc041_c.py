n = int(input())
a = list(map(int, input().split()))
b = sorted(a, reverse=True)
for i in b:
    print(a.index(i) + 1)
