n = int(input())
a = list(map(int, input().split()))
print(max(a.count(i-1) + a.count(i) + a.count(i+1) for i in range(1, 100001)))
