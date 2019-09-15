n = int(input())
a = list(map(int, input().split()))
print(sum((i - round(sum(a)/n)) ** 2 for i in a))
