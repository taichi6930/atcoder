a, b, c, x, y = map(int, input().split())

# ABピザを買うかA,Bピザを買うか
cNum = min(x // 2, y // 2) * 2
print(min(a + b, c * 2) * cNum + (x-cNum) *
      min(a, c * 2) + (y-cNum) * min(a, c * 2))
