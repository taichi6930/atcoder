abcList = [[4, 6, 9, 11], [2]]
x, y = map(int, input().split())
a = (abcList[0].count(x) == abcList[0].count(y))
b = (abcList[1].count(x) == abcList[1].count(y))
print("Yes" if (a and b) else "No")
