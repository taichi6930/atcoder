import math
n = int(input())
aList = list(map(int, input().split()))
print(int(math.ceil(sum(aList)/(n - aList.count(0)))))
