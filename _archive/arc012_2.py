n, va, vb, l = map(int, input().split())

a, b = 0, l

for i in range(n):
    t = l / va
    a += t * va
    b += t * vb
    l = b - a

print(l)
