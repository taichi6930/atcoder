from math import floor

h = int(input())
hSum = 0
for i in range(10**12):
    hSum += 2 ** i
    h = floor(h/2)
    if h == 0:
        break

print(hSum)
