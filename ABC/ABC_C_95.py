a, b, c, x, y = map(int, input().split())

# ABピザを買うかA,Bピザを買うか
cNum = min(x // 2, y // 2) * 2
print(cNum, min(a + b, c * 2) * cNum, (a) * (x - cNum), (b) * (y - cNum))
