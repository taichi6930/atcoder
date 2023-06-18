n = int(input())
aList = list(map(int, input().split()))
print(3 ** n - 2 ** [2 if aList[i] % 2 == 0 else 1 for i in range(n)].count(2))
