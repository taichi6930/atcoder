n = int(input())
a = list(map(int, input().split()))
b = [None] * n
print(a.index(1) + 1, end=" ")
for i in range(1, n):
    print(a.index(i + 1) + 1, end=" ")
print("")
