n = int(input())
aList = [int(input()) for i in range(n)]
print(len(aList) - len(set(aList)))
