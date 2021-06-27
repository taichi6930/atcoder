n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

print(sum([abs(a[i] - b[i]) for i in range(n)]))
