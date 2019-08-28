s = input()
alphaList = ["A", "B", "C", "D", "E", "F"]
print(*[s.count(alphaList[i]) for i in range(6)])
