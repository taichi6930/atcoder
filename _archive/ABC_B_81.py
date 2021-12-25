n = int(input())
a = list(map(int, input().split()))
aMin = 30
for i in a:
    aCnt = 0
    while n > 0:
        if i % 2 != 1:
            aCnt += 1
            i /= 2
        else:
            break
    if aCnt < aMin:
        aMin = aCnt
print(aMin)
