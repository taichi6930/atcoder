n = int(input())
a = [None] * n
b = [None] * n

for i in range(n):
    a[i], b[i] = map(int, input().split())

aMin = min(a)
bMin = min(b)

if a.index(aMin) != b.index(bMin):
    print(max(aMin, bMin))
    exit()

minab = aMin + bMin

a.pop(a.index(aMin))
b.pop(b.index(bMin))

a2Min = min(a)
b2Min = min(b)

print(min(minab, max(a2Min, bMin), max(aMin, b2Min)))
