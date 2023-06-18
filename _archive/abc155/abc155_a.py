aList = list(map(int, input().split()))
print("YNeos"[len(aList) - len(set(aList)) != 1::2])
