n, k = map(int, input().split())
hList = sorted(map(int, input().split()), reverse=True)
afterhList = hList[k:n]
afterhListSum = sum(afterhList)
print(afterhListSum)
