import math as m

n = int(input())
minN = n
nSqrtMax = m.floor(m.sqrt(n))

for i in range(nSqrtMax):
    if n // (nSqrtMax - i) - (nSqrtMax - i) > minN:
        break
    a = abs(n // (nSqrtMax - i) - (nSqrtMax - i)) + n % (nSqrtMax - i)
    minN = min(minN, a)
print(minN)
