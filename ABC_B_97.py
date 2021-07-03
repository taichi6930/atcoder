x = int(input())
xMax = 0
for i in range(2, 10):
    for j in range(33):
        if j ** i <= x and xMax < j ** i:
            xMax = j ** i

print(xMax)
