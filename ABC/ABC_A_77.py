sList = [list(input()) for _ in range(2)]
print("YES" if sList[0][2] == sList[1][0] and sList[0][1]
      == sList[1][1] and sList[0][0] == sList[1][2] else "NO")
