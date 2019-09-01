x, y = map(str, input().split())
alphaList = ["A", "B", "C", "D", "E", "F"]
ans = alphaList.index(x) - alphaList.index(y)
print("<" if ans < 0 else ">" if ans > 0 else "=")
